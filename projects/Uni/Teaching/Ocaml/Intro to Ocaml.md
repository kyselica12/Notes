---
height: "540" 
theme: white
css: [css/layout.css,css/custom_layout.css]
---

<!-- slide template="[[title-slide]]" -->

::: title
A Tour of OCaml
:::
 


::: event
FPRO 2024
:::



::: author
Daniel Kyselica
:::

::: date
9.5.2024
:::

::: footer

:::
 
<grid drag="50 50"  drop="40 30">
![[Pasted image 20240507130050.png]]
</grid>


---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Why OCaml?
:::


<grid drag="45 100"  drop="0 10">
+ Functional
+ Strict typing
+ Object oriented
+ Fast
+ Strong compilation (even WASM)
</grid>
<grid drag="50 100"  drop="45 10">
![[Pasted image 20240507150733.png]]
</grid>

::: footer

:::

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Usage
:::
<grid drag="44 80"  drop="0 15">
![[Pasted image 20240509100758.png|250]]
![[Pasted image 20240509100845.png|300]]
</grid>

<grid drag="40 100"  drop="55 0">
![[Pasted image 20240509100517.png]]
![[Pasted image 20240509100552.png]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-nosubtitle]]" -->

::: title
History
:::

<grid drag="60 100"  drop="0 0">
- 1980s Categorical Abstract Machine (CAM)
- 1987 Caml - first implementation by Gerard Huet
- 1995 Caml Special Light - improved version of Caml
- 2011 Ocaml - Objective Caml
</grid>

<grid drag="30 100"  drop="65 0">
![[Pasted image 20240509101747.png]]
</grid>
::: footer
:::

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
First program
:::
::: footer
:::


```
$ opam exec -- dune init proj hello
Success: initialized project component named hello
```

```
├── bin
│   ├── dune
│   └── main.ml
├── _build
│   └── log
├── dune-project
├── hello.opam
├── lib
│   └── dune
└── test
    ├── dune
    └── hello.ml
```

---

<!-- slide template="[[basic-slide]]" -->

::: title
Main.ml
:::

::: subTitle
First program
:::

::: footer
:::

```
let () = print_endline "Hello, World!"
```

```
$ opam exec -- dune build
$ opam exec -- dune exec hello
Hello, World!
```

---

<!-- slide template="[[basic-slide]]" -->

::: title
Expressions and Definitions
:::
::: subTitle
Tour of Ocaml
:::

Types
- int 
- float
- string
- bool
- list 
- ...

<grid drag="50 100"  drop="50 0">
**Let**
```ocaml
let x = 50
let z = 9 :: [1,3,5,6]
let r = 2 * if "hello" = "world" then 3 else 5
let a = 2.0 +. 2.0
```
**In**
```ocaml
# let a = 1 in
  let b = 2 in
    a + b;;
- : int = 3
```

</grid>

::: footer
:::



---

<!-- slide template="[[basic-slide]]" -->

::: title
Functions
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="50 100"  drop="0 0" align="top" >
**Definition**
```ocaml
# let square x = x * x;;
val square : int -> int = <fun>

# square 50;;
- : int = 2500
```
**Anonymus**
```ocaml
# (fun x -> x * x) 50;;
- : int = 2500
```

</grid>
<grid drag="50 100"  drop="50 0" align="top">
**Recursive**
```ocaml
# let rec range lo hi =
    if lo > hi then
      []
    else
      lo :: range (lo + 1) hi;;
val range : int -> int -> int list = <fun>
```
**Side-Effects - unit Type**
```ocaml
# read_line;;
- : unit -> string = <fun>
```
</grid>

---

<!-- slide template="[[basic-slide]]" -->

::: title
Functions
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="50 100"  drop="0 0" align="top" >

**Labeled arguments**
```ocaml
# StringLabels.sub;;
- : string -> pos:int -> len:int -> string = <fun>

# let f ~x ~y = x - y
val f : x:int -> y:int -> int = <fun>

# let x = 3 and y = 2 in f ~x ~y
- : int = 1
```
</grid>
<grid drag="50 100"  drop="50 0" align="top">
**Optional arguments**
```ocaml
# let bump ?(step = 1) x = x + step;;

val bump : ?step:int -> int -> int = <fun>
```
</grid>

---

<!-- slide template="[[basic-slide]]" -->

::: title
Lists & Tuples
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="50 100"  drop="0 0" align="top" >

```ocaml
# [];;
- : 'a list = []

# [1; 2; 3];;
- : int list = [1; 2; 3]

# [false; false; true];;
- : bool list = [false; false; true]

# [[1; 2]; [3]; [4; 5; 6]];;
- : int list list = [[1; 2]; [3]; [4; 5; 6]]

# 1 :: [2; 3; 4];;
- : int list = [1; 2; 3; 4]
```
```ocaml
# let snd p =
    match p with
    | (_, y) -> y;;
val snd : 'a * 'b -> 'b = <fun>
```
</grid>
<grid drag="50 100"  drop="50 0" align="top">
**Patern matching**
```ocaml
# let rec sum u =
    match u with
    | [] -> 0
    | x :: v -> x + sum v;;
val sum : int list -> int = <fun>

# sum [1; 4; 3; 2; 5];;
- : int = 15

# #show option;;
type 'a option = None | Some of 'a

# let f opt = match opt with
    | None -> None
    | Some None -> None
    | Some (Some x) -> Some x;;
val f : 'a option option-> 'a option = <fun>
```

</grid>

---

<!-- slide template="[[basic-slide]]" -->

::: title
Types & Records
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="50 100"  drop="0 0" align="top" >
**Types**
```ocaml
# type primary_colour = Red | Green | Blue;;
type primary_colour = Red | Green | Blue

# [Red; Blue; Red];;
- : primary_colour list = [Red; Blue; Red]
```
```ocaml
# let colour_to_rgb colour =
    match colour with
    | Red -> (0xff, 0, 0)
    | Green -> (0, 0xff, 0)
    | Blue -> (0, 0, 0xff);;
val colour_to_rgb : primary_colour -> int * int * int 
= <fun>
```
</grid>
<grid drag="50 100"  drop="50 0" align="top">
**Records**
```ocaml
type person = {
    first_name : string;
    surname : string;
    age : int
  }
let gerard = {
     first_name = "Gérard";
     surname = "Huet";
     age = 76
  }
```
```ocaml
let is_teenager person =
    match person with
    | { age = x; _ } -> 13 <= x && x <= 19;;
```
</grid>
---

<!-- slide template="[[basic-slide]]" -->

::: title
Mutable state
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="40 100"  drop="0 0" align="top" >
**Reference**
```ocaml
# let r = ref 0;;
val r : int ref = {contents = 0}
```
```ocaml
# !r;;
- : int = 0
```
</grid>
<grid drag="60 100"  drop="40 0" align="top">
**Update**
```ocaml
# r := 42;;
- : unit = ()
```
```ocaml
# let text = ref "hello ";;
val text : string ref = {contents = "hello "}

# print_string !text; text := "world!"; print_endline !text;;
hello world!
- : unit = ()
```
</grid>


---
<!-- slide template="[[basic-slide]]" -->

::: title
Modules
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

```ocaml
# #show Option;;
module Option :
  sig
    type 'a t = 'a option = None | Some of 'a
    val none : 'a t
    val some : 'a -> 'a t
    val value : 'a t -> default:'a -> 'a
    val get : 'a t -> 'a
    val bind : 'a t -> ('a -> 'b t) -> 'b t
    val join : 'a t t -> 'a t
    val map : ('a -> 'b) -> 'a t -> 'b t
    val fold : none:'a -> some:('b -> 'a) -> 'b t -> 'a
    val iter : ('a -> unit) -> 'a t -> unit
    val is_none : 'a t -> bool
    val is_some : 'a t -> bool
    val equal : ('a -> 'a -> bool) -> 'a t -> 'a t -> bool
    val compare : ('a -> 'a -> int) -> 'a t -> 'a t -> int
    val to_result : none:'e -> 'a t -> ('a, 'e) result
    val to_list : 'a t -> 'a list
    val to_seq : 'a t -> 'a Seq.t
  end
```


---
<!-- slide template="[[basic-slide]]" -->

::: title
Loops
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

```ocaml
for variable = start_value to end_value do
  expression
done

for variable = start_value downto end_value do
  expression
done
```

```
while boolean-condition do
  expression
done
```
---

<!-- slide template="[[basic-slide]]" -->

::: title
Class
:::
::: subTitle
Tour of Ocaml
:::
::: footer
:::

<grid drag="61 100"  drop="0 0" align="left" >
```ocaml
# class stack_of_ints =
  object (self)
    val mutable the_list = ([] : int list)     (* instance variable *)
    method push x =                            (* push method *)
      the_list <- x :: the_list
    method pop =                               (* pop method *)
      let result = List.hd the_list in
      the_list <- List.tl the_list;
      result
    method peek =                              (* peek method *)
      List.hd the_list
    method size =                              (* size method *)
      List.length the_list
  end;;
class stack_of_ints :
  object
    val mutable the_list : int list
    method peek : int
    method pop : int
    method push : int -> unit
    method size : int
  end
```
</grid>
<grid drag="41 100"  drop="57 0" align="top">
```ocaml
# for i = 1 to 10 do
    s#push i
  done;;
- : unit = ()
# while s#size > 0 do
    Printf.printf "Popped %d off the stack.\n" s#pop
  done;;
Popped 10 off the stack.
Popped 9 off the stack.
Popped 8 off the stack.
Popped 7 off the stack.
Popped 6 off the stack.
Popped 5 off the stack.
Popped 4 off the stack.
Popped 3 off the stack.
Popped 2 off the stack.
Popped 1 off the stack.
- : unit = ()
```
</grid>
