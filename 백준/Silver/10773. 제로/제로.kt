fun main() {
    val k : Int = readLine()!!.toInt()
    val writeList = mutableListOf<Int>()

    repeat(k) {
        val n : Int = readLine()!!.toInt()

        if (n == 0 && writeList.isNotEmpty()) {
            writeList.removeAt(writeList.size-1)
        } else {
            writeList.add(n)
        }
    }
    print(writeList.sum())
}