---
height: "800" 
theme: white
css: []
---
# test
```kotlin
fun main() {
    val N = 10
    val M = 1000

    val results = IntArray(N * 6)

    //rolls
    for (i in 1..M){
        //roll dice
        var res = 0
        for (j in 1..N)
            // zbytocne vytvaranie noveho listu
            res += listOf(1, 2, 2, 3, 3, 3, 4, 4, 4, 4,
             5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6).random();
            //res += (1..6).random();

        results[res] = results[res] + 1
    }

    for (i in 0..<(N*6)){
        println((i+1).toString() + "*".repeat(results[i]));
    }
}
```

---
# test2
```kotlin
fun main() {
    val N = 10
    val M = 1000
    val n_sides = 6

    // val vals = listOf(1, 2, 2, 3, 3, 3, 4, 4, 4, 4,
     5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6);

    val vals = (1..n_sides).map {i -> List(i) { i }}
			   .flatten();

    val results = IntArray(M){i->i}
                  .map {IntArray(N) {vals.random();}.sum()}
                  .groupingBy{it}.eachCount();
    
    print(results)
}
```