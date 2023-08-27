fun main() {
    val t: Int = readLine()!!.toInt()

    for (i in 0 until t) {
        val (n, m) = readLine()!!.split(" ").map(String::toInt)
        //String::toInt는 함수 참조 문법으로, 문자열을 정수로 변환하는 함수를 가리킴.

        for (j in 0 until m) {
            val (a, b) = readLine()!!.split(" ").map(String::toInt)
        }

        println(n-1)
    }
}