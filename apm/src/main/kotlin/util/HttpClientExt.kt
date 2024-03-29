package util

import io.ktor.client.HttpClient
import io.ktor.client.engine.apache.Apache
import io.ktor.client.features.json.Json
import io.ktor.client.features.json.serializer.KotlinxSerializer
import io.ktor.http.ContentType

fun createHttpClient(
    connectionTimeout: Int = 5_000
) = HttpClient(Apache) {
    Json {
        serializer = KotlinxSerializer(kotlinx.serialization.json.Json {
            prettyPrint = true
            isLenient = true
            ignoreUnknownKeys = true
        })
        accept(ContentType.Any)
    }
    engine {
        socketTimeout = connectionTimeout
        connectTimeout = connectionTimeout
        connectionRequestTimeout = connectionTimeout * 2
    }
    expectSuccess = false
}