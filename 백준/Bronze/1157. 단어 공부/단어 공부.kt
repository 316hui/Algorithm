fun main() {
    val words = readLine()!!.toUpperCase()
    val uniqueWords = words.toSet().toList()

    val cntList = mutableListOf<Int>()

    for (x in uniqueWords) {
        val cnt = words.count { it == x}
        cntList.add(cnt)
    }

    if (cntList.count {it == cntList.maxOrNull()} > 1) {
        print("?")
    }else {
        val maxIndex = cntList.indexOf(cntList.maxOrNull())
        println(uniqueWords[maxIndex])
    }
}