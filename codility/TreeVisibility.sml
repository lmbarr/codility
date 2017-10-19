
datatype Node = N of int * Node * Node | Leaf of int * Node option * Node option
exception Error
fun number_of_visible_nodes e =
    let
        val N(value, l, r) = e
        fun f(exp, max_value) =
            case exp of
              Leaf(i, NONE, NONE) => 0
            | N(i, l, r) => if i >= max_value
                            then 1 + f(l, i) + f(r, i)
                            else 1 + f(l, max_value) + f(r, max_value)
            | _ => raise Error
    in
    f(e, value)
    end

val f = N(8, N(2, Leaf(8, NONE, NONE), Leaf(7, NONE, NONE)), Leaf(6, NONE, NONE))
val g = number_of_visible_nodes f
val h = N(5, N(3, Leaf(20, NONE, NONE), Leaf(21, NONE, NONE)), Leaf(10, Leaf(1, NONE, NONE), NONE))
