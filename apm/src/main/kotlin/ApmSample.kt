@file:JvmName("ApmSample")

import io.ktor.client.HttpClient
import io.ktor.client.request.get
import io.ktor.client.request.post
import io.ktor.http.ContentType
import io.ktor.http.contentType
import kotlinx.coroutines.delay
import util.createHttpClient
import util.withJsonSupport
import kotlin.system.exitProcess
import kotlin.time.Duration
import kotlin.time.ExperimentalTime

private val httpClient = createHttpClient().withJsonSupport()
private val operationIds: MutableList<String> = ArrayList()

@OptIn(ExperimentalTime::class)
suspend fun main() {
    var inputApiUrl: String
    do {
        print("Input the APM API url (default: http://localhost:8080/api): ")
        inputApiUrl = readLine()!!.ifBlank { "http://localhost:8080/api" }.trim()
    } while (!checkApiConnection(inputApiUrl))

    var miningOperationsCount: String
    var altchainName: String
    do {
        print("How many mining operations do you want to start? (default: 1): ")
        miningOperationsCount = readLine()!!.ifBlank { "1" }

        print("Input the altchain name (default: vbtc): ")
        altchainName = readLine()!!.ifBlank { "vbtc" }
    } while (!startMiningOperation(inputApiUrl, miningOperationsCount, altchainName))

    print("Do you want to track the operations status? (default: yes): ")
    val trackStatus = readLine()!!.ifBlank { "yes" }.startsWith("y")
    if (trackStatus) {
        println("This operation can take a while...")
        val operationTrack = httpClient.getAllOperations(inputApiUrl).operations.asSequence().filter {
            operationIds.contains(it.operationId)
        }.associate {
            it.operationId to it.task
        }.toMutableMap()

        while (operationTrack.any { it.value != "Detect Payout" }) {
            operationTrack.forEach { (operationId, operationTask) ->
                val operationDetailResponse = httpClient.getOperationDetails(inputApiUrl, operationId)
                if (operationTask != operationDetailResponse.task) {
                    println("Operation id: $operationId is now running the task: ${operationDetailResponse.task}")
                    operationTrack[operationDetailResponse.operationId] = operationDetailResponse.task
                }
            }
            delay(Duration.seconds(1))
        }
        println("All the operations have been completed!")
    } else {
        exitProcess(1)
    }
}

private suspend fun HttpClient.getMinerData(url: String) =
    get<MinerInfoResponse>("$url/miner")

private suspend fun HttpClient.startMiningOperation(url: String, request: MineRequest) =
    post<OperationSummaryResponse>("$url/miner/mine") {
        contentType(ContentType.Application.Json)
        body = request
    }

private suspend fun HttpClient.getConfiguredAltChains(url: String) =
    get<ConfiguredAltchainList>("$url/miner/configured-altchains")

private suspend fun HttpClient.getAllOperations(url: String) =
    get<OperationSummaryListResponse>("$url/miner/operations")

private suspend fun HttpClient.getOperationDetails(url: String, id: String) =
    get<OperationDetailResponse>("$url/miner/operations/$id")

private suspend fun HttpClient.getNetwork(url: String) =
    get<NetworkInfoResponse>("$url/network")

private suspend fun checkApiConnection(url: String): Boolean = try {
    val networkInfoResponse = httpClient.getNetwork(url)
    println("Connected to the APM miner API, the miner is running on the ${networkInfoResponse.name} network!")
    true
} catch(exception: Exception) {
    print("Couldn't connect to the APM API with the supplied url (${exception.message}), do you want to review the configuration? (default: no): ")
    if (!readLine()!!.startsWith("y")) {
        exitProcess(1)
    }
    false
}

private suspend fun startMiningOperation(url: String, count: String, altchainName: String): Boolean {
    try {
        operationIds.clear()
        val operationCount = count.toInt()

        val minerStatus = httpClient.getMinerData(url)
        if (!minerStatus.status.isReady) {
            print("The APM miner is not ready: ${minerStatus.status.reason}, do you want to try again? (default: no): ")
            if (!readLine()!!.startsWith("y")) {
                exitProcess(1)
            }
            return false
        }

        val configuredAltchains = httpClient.getConfiguredAltChains(url)
        if (configuredAltchains.altchains.find { it.key == altchainName } == null) {
            print("The $altchainName altchain is not configured, do you want to try again? (default: no): ")
            if (!readLine()!!.startsWith("y")) {
                exitProcess(1)
            }
            return false
        }

        repeat(operationCount) {
            val operation = httpClient.startMiningOperation(url, MineRequest(altchainName))
            operationIds.add(operation.operationId)
            println("Started operation id: ${operation.operationId}")
        }

        return true
    } catch (exception: Exception) {
        return false
    }
}
