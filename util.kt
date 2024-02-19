import java.io.BufferedWriter
import kotlin.math.sqrt
import kotlin.math.pow


val Int.isEven: Boolean
    get() = this % 2 == 0

val Int.isPrime: Boolean
    get() {
        for (delimiter in 2..sqrt(this.toDouble()).toInt()) {
            if (this % delimiter == 0) return false
        }

        return true
    }

fun Int.pow(n: Int): Int {
    return this.toDouble().pow(n).toInt()
}

fun gcd(a: Int, b: Int): Int {
    val remainder = a % b
    return if (remainder == 0) b else gcd(b, remainder)
}


fun c(n: Long, k: Long): Long {
    return factorial(n) / (factorial(k) * factorial(n - k))
}

fun factorial(n: Long): Long {
    var result = 1L
    for (i in 2..n) {
        result *= i
    }
    return result
}


fun String.replaceLast(oldValue: String, newValue: String): String {
    if (!contains(oldValue)) return this

    return substringBeforeLast(oldValue) + newValue + substringAfterLast(oldValue)
}


fun <E> Collection<E>.isSub(collection: Collection<E>): Boolean {
    for (element in this.toSet()) {
        if (collection.count { it == element } < this.count { it == element }) {
            return false
        }
    }
    return true
}

fun <T> List<List<T>>.tableString(columnSeparator: String = "\t", rowSeparator: String = "\n"): String {
    return this.joinToString(rowSeparator) { it.joinToString(columnSeparator) }
}


fun BufferedWriter.writeLn(line: String) {
    write(line)
    newLine()
}


/**
 * Returns a list of lists, each built from elements of all lists with the same indexes.
 * Output has length of the shortest input list.
 */
fun <T> zip(vararg lists: List<T>): List<List<T>> {
    return zip(*lists, transform = { it })
}

/**
 * Returns a list of values built from elements of all lists with same indexes using provided [transform].
 * Output has length of the shortest input list.
 */
fun <T, V> zip(vararg lists: List<T>, transform: (List<T>) -> V): List<V> {
    val minSize = lists.minOfOrNull(List<T>::size) ?: return emptyList()
    val iterators = lists.map { it.iterator() }

    return List(minSize) { transform(iterators.map { it.next() }) }
}
