fun main() {
    val n = readLine()!!.toInt()

    repeat(n) {
        val num = readLine()!!.toInt()
        val lenNum = num.toString().length

        if ((num * num).toString().takeLast(lenNum) == num.toString()) {
            println("YES")
        } else {
            println("NO")
        }
    }
}
