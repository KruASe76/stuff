val workerNames = listOf("дедка", "бабка", "внучка", "Жучка", "кошка", "мышка")

fun main() {
    println("Посадил дед репку.")
    println("И выросла репка большая-пребольшая.")

    print("\t(введите минимальную силу, чтобы вытянуть выросшую репку): ")
    val repkaPower = readln().toInt()

    println("Пошел ${workerNames[0]} её тянуть.")
    print("\t(введите силу ${workerNames[0].relativeCase}): ")
    val ded = Worker(workerNames[0], readln().toInt(), null)

    workerNames
        .windowed(2)
        .forEach { (currentWorkerName, nextWorkerName) ->
            if (ded.totalPower >= repkaPower) {
                println(
                    if (ded.next == null)
                        "Тянет-потянет — вытянул репку!"
                    else
                        "тянут-потянут — вытянули репку!"
                )
                return
            } else {
                println(
                    if (ded.next == null)
                        "Тянет-потянет, вытянуть не может!"
                    else
                        "тянут-потянут, вытянуть не могут!"
                )
            }

            println("Позвал${if (ded.next == null) "" else ""} $currentWorkerName ${nextWorkerName.accusativeCase}.")
            print("\t(введите силу ${nextWorkerName.relativeCase}): ")
            ded.lastWorker.next = Worker(nextWorkerName, readln().toInt(), ded.lastWorker)

            ded.lastWorker.pullString.let { pullString ->
                println("${pullString.first().uppercase()}${pullString.drop(1)} —")
            }
        }
    println("тянут-потянут, вытянуть не могут!")

    println()

    println("Рабочая сила кончилась, репка не вытянута.")
    println("MISSION FAILED")
}


data class Worker(
    private val name: String,
    private val power: Int,
    private val previous: Worker?,
    var next: Worker? = null
) {
    val totalPower: Int
        get() = power + (next?.totalPower ?: 0)

    val lastWorker: Worker
        get() = next?.lastWorker ?: this

    val pullString: String
        get() =
            if (previous != null)
                "$name за ${previous.name.accusativeCase},\n${previous.pullString}"
            else
                "$name за репку"
}


val String.relativeCase: String
    get() = replaceLast("а", "и")

val String.accusativeCase: String
    get() = replaceLast("а", "у")


fun String.replaceLast(oldValue: String, newValue: String): String {
    if (!contains(oldValue)) return this

    return substringBeforeLast(oldValue) + newValue + substringAfterLast(oldValue)
}
