fun main() {
    var n = readLine()!!
    var cnt = 0

    while (n.length > 1) {
        var summ = 0
        for (i in 0 until n.length) {
            summ += n[i].toString().toInt()
        }
        n = summ.toString()
        cnt ++
    }
    println(cnt)

    if (n.toInt() % 3 == 0){
        println("YES")
    } else {
        print("NO")
    }
}