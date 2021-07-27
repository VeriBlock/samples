import kotlinx.serialization.Serializable

@Serializable
data class MinerInfoResponse(
    val vbkAddress: String,
    val vbkBalance: Long,
    val status: MinerStatusResponse
)

@Serializable
data class MinerStatusResponse(
    val isReady: Boolean,
    val reason: String? = null
)

@Serializable
data class MineRequest(
    val chainSymbol: String,
    val height: Int? = null
)

@Serializable
data class OperationSummaryResponse(
    val operationId: String,
    val chain: String,
    val endorsedBlockHeight: Int? = null,
    val state: String,
    val task: String
)

@Serializable
data class ConfiguredAltchainList(
    val altchains: List<ConfiguredAltchain>
)

@Serializable
data class ConfiguredAltchain(
    val id: Long,
    val key: String,
    val name: String,
    val payoutDelay: Int,
    val syncStatus: AltChainSyncStatusResponse,
    val readyStatus: AltChainReadyStatusResponse,
    val explorerBaseUrls: ExplorerBaseUrlsResponse
)

@Serializable
data class AltChainReadyStatusResponse(
    val isReady: Boolean,
    val reason: String? = null
)

@Serializable
data class AltChainSyncStatusResponse(
    val networkHeight: Int,
    val localBlockchainHeight: Int
)

@Serializable
data class ExplorerBaseUrlsResponse(
    val blockByHeight: String? = null,
    val blockByHash: String? = null,
    val transaction: String? = null,
    val address: String? = null,
    val atv: String? = null
)

@Serializable
data class OperationSummaryListResponse(
    val operations: List<OperationSummaryResponse>,
    val totalCount: Int
)

@Serializable
data class OperationDetailResponse(
    val operationId: String,
    val chain: String,
    val endorsedBlockHeight: Int? = null,
    val state: String,
    val task: String,
    val stateDetail: Map<String, String>
)

@Serializable
data class NetworkInfoResponse(
    val name: String,
    val explorerBaseUrls: ExplorerBaseUrlsResponse
)