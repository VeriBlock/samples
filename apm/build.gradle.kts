plugins {
    java
    kotlin("jvm") version "1.5.20"
    idea
    application
    kotlin("plugin.serialization") version "1.5.20"
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenLocal()
    maven("https://jitpack.io")
    jcenter()
}

dependencies {
    // Kotlin
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.5.20")
    implementation("org.jetbrains.kotlin:kotlin-reflect:1.5.20")

    // HTTP Client
    implementation("io.ktor:ktor-client-apache:1.6.1")
    implementation("io.ktor:ktor-client-serialization:1.6.1")

    // Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.5.0")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-jdk8:1.5.0")

    // Serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.2.1")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-protobuf:1.2.1")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-hocon:1.2.1")
}

application.applicationName = "apm"
application.mainClassName = "ApmSample"
