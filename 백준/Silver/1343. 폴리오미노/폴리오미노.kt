fun main() {
    val s = readLine()!!

    var String = s.replace("XXXX","AAAA")
    String = String.replace("XX","BB")
    //AAAA로 바꾸고 남은 값을 마저 BB로 바꿔줌

    if ("X" in String) {
        print(-1)
    } else {
        println(String)
    }

}