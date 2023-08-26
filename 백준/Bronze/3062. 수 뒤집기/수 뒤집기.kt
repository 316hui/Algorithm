fun main() {
    val n = readLine()!!.toInt()

    repeat(n) {
        val num = readLine()!!
        val reverseNum = num.reversed()

        val sum = num.toInt() + reverseNum.toInt()

        if (sum.toString() == sum.toString().reversed()) {
            println("YES")
        } else {
            println("NO")
        }
    }
}
