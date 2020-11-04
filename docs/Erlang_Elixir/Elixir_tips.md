
## 1. not not == true !! (Double Bang)
It is handy when a bounded value results to nil, true, false, and some_value.Assume that you have to return truthness of a boolean based on this bounded value.
Following are the examples of a value and it’s output.
```Elixir
value = nil      :: false
value = false    :: false
value = true     :: true
value = anything :: true
```

**Before**
```Elixir
staus = 
  if not is_nil(value) && value do
    true
  else
    false
  end    
```  

**Hack**
```Elixir
status = !!value
```
We have completely replaced the if macro here.

## 2. Boolean Conversion

If value is "True" (string format) it has to return true else false booleans.
**Before**
```Elixir
status = 
  if value == "True" do
    true
  else
    false
  end
```

**Hack**
```Elixir
status = value == "True"
```

## 3. Replacing cond with && — Boolean Evaluation

This is a versatile check for a key in a map existence and it’s value truthness.
Before understanding this logic, we need to know defference between `and` and `&&`. The and expects boolean and `&&` can be `any()`. So, we are making use of `&&` for the following requirement.

**Requirement**
The requirement is to check a key in a map.
**Check 1**: If the **key** exists and it is not neither `nil` nor `false` then I have to execute a statement.
**Check 2**: If the **key** is not present in a map or if it’s **value** is `nil` then it has to return `nil`.
**Check 3**: If the **key** exists and value is `false` then it has to return `false`.
I’ll make use of the following examples named as the serve.

```Elixir
nil_map = %{name: "Blackode", balance: nil}
false_map = %{name: "Blackode", balance: false}
key_miss_map = %{name: "Blackode"}
balance_map = %{name: "Blackode", balance: 2500000}
```

So, our data can beone of the above maps.

```Elixir
data :: nil_map | false_map | key_miss_map | balance_map
```

**Before**
```Elixir
status = 
  cond do
    is_nil(data[:balance]) -> 
      nil
    data[:balance] == false -> 
      false
    true ->
      "Hurray! I have balance"
  end
```
This is a very typical case to understand. We cannot use our Double Bang hack here as it always returns either `false/true` but, we need `nil` as well. So, we go for the following trick which simply uses `&&` operator

**Hack**
```Elixir
status = data[:balance] && "Hurray! I have balance"
```

BTW, we cannot use `and` operator here as it always expects a boolean in left side. But, in our case, we get `nil` as well. We completely replaced multiple conditons.
You can apply this logic by just remembering the thumb rule that the short circuit operators will execute only if the left side value is not enough to decide the result.

**Examples**
```Elixir
data[:balance] && big_function_calling()
```
Here 👆 left side is `data[:balance]` and `&&` expects both sides must evaluate their trutheness to be `true`. If `data[:balance]` value is either `nil` nor `false`, then it won’t execute `big_calling_function()` as `data[:balance]` is enough to give the result as its truthness is `false` So, it gives the ouput of the `data[:balance]` as a result.


## Elixir Tip: Case vs. With

Use case when you need to perform exhaustive pattern matching, and ensure that at least one of the conditions matches:
```Elixir
case foo() do
  cond1 -> expression1
  cond2 -> expression2
  cond3 -> expression3
  _ -> default_expression
end
```

A very common use case is to pattern match on the results of potentially error-prone operations:
```Elixir
case foo() do
  {:ok, res} -> do_something_with_result(res)
  {:error, err} -> handle_error(err)
end
```

So far, so good. Now, we come to a very common daily work scenario. Imagine that we have one such operation (e.g. external API call, IO or DB operation, etc), and we want to perform a second such operation, but only if the first one were successful. How do we do that?
Recall that conditionals in Elixir are functions too. They can be piped into, or chained in the expression part of other conditionals. This allows us to to solve our problem above using chained conditionals:
```Elixir
case foo() do
  {:ok, res} ->
    case bar(res) do
	  {:ok, res2} -> do_something_with_result(res2)
	  {:error, err} -> handle_error(err)
	end
  {:error, err} -> handle_error(err)
end
```

Even with only two such calls, the level of complexity rose drastically. Add just one more such call, and the code becomes unreadable:
```Elixir
case foo() do
  {:ok, res} ->
    case bar(res) do
	  {:ok, res2} ->
        case baz(res2) do
          {:ok, res3} -> do_something_with_result(res3)
          {:error, err} -> handle_error(err)
        end
	  {:error, err} -> handle_error(err)
	end
  {:error, err} -> handle_error(err)
end
```

**`with` to the rescue**

This is where the with operator gets really handy. In its basic form, it resembles our chained case above, but in a way, also functions like a pipeline operator. Check this out:
```Elixir
with {:ok, res} <- foo(),
     {:ok, re2} <- bar(res)
     {:ok, re3} <- baz(re2) do
  do_something_with_result(res3)
end
```
This shall be interpreted as, “do all the comma separated operations in sequence, and if the previous one has matched, execute the next one. Finally, run the code inside the do/end block". This looks much more succinct and readable than its version before, but it has another big advantage too. It allows the programmer to focus on the happy-end business scenarios first. Some of you might have been wondering what would happen, if any of the comma-separated operations returns and {:error, err} tuple instead. The answer is, the first non-matching expression will be returned. In simple terms, if we don't care about the outcome of non-ok results, we might as well leave the happy path and leave it to the caller to take care of the final result.
If you have worked with Phoenix, you might recall that this is exactly how its fallback actions work. In our controller actions, we take care of the happy path, and if an error occurs, Phoenix will pattern-match one of our fallback actions to take care of it instead:
```Elixir
defmodule MyController do
  use Phoenix.Controller

  action_fallback MyFallbackController

  def show(conn, %{"id" => id}, current_user) do
    with {:ok, post} <- Blog.fetch_post(id),
         :ok <- Authorizer.authorize(current_user, :view, post) do

      render(conn, "show.json", post: post)
    end
  end
end
```

Fallback controller example from the official Phoenix docs

**`with`/`else`**

If we want to take care of side effects ourselves, with offers an expanded version:
```Elixir
with {:ok, res} <- foo(),
     {:ok, res2} <- bar(res) do
  do_something_with_res(res2)
else
  {:error, {:some_error, err}} -> handle_some_error(err)
  {:error, {:some_other_error, err}} -> handle_some__other_error(err)
  default -> handle_something_completely_unexpected(default)
end
```
> NOTE: Keep in mind that while the simple with form won’t throw an error when no match occurs, when using else you have to exhaustively match all cases.

**When not to use `with`**

Using a single pattern-matching clause with else:
This will make the code more difficult to read than you need it to be. The code below:
```Elixir
with {:ok, res} <- foo() do
  do_something_with_res(res)
else
  {:error, {:some_error, err}} -> handle_some_error(err)
end
```
Can easily be replaced with a more readable case block:
```Elixir
case foo() do
  {:ok, res} -> do_something_with_res(res)
  {:error, {:some_error, err}} -> handle_some_error(err)
end
```

## alias `__MODULE__`

`alias __MODULE__, as: SomeOtherName`
or
```Elixir
defmodule API.User do
  alias __MODULE__

  defstruct name: nil, age: 0

  def old?(%User{name: name, age: age} = user) do
    ...
  end
end
```

## defstruct with `@enforce_keys`

```Elixir
def new(status) do
  %Game{status: status}
end

iex> Fun.Game.new(:won)
iex> %Fun.Game{status: :won, time: nil}
```

## `v()` function in `iex`

When you want to start the server and check the result in iex you can use v() to return the result from last command:

```Elixir
iex(1)> Metex.Worker.start_link()
{:ok, #PID<0.472.0>}
iex(2)> {:ok, pid} = v()
{:ok, #PID<0.472.0>}
iex(3)>  pid
#PID<0.472.0>
```

## bind value to an optional variable

You can bind a value to an optional variable like this:
```Elixir
_dont_care = 1
```
And you can apply this trick to our functions to make them more readable:

```Elixir
defp accept_move(game, _guess, _already_used = true) do
  Map.put(game, :state, :already_used)
end
defp accept_move(game, guess, _not_used) do
  Map.put(game, :used, MapSet.put(game.used, guess))
  |> score_guess(Enum.member?(game.letters, guess))
end
```

##

## Links

https://medium.com/@blackode/3-elixir-pro-boolean-hacks-4c1884cd4f5f
https://github.com/blackode/elixir-tips
https://dockyard.com/blog/2020/07/27/5-elixir-tips-learned-in-code-review
https://medium.com/swlh/elixir-tip-case-vs-with-28b04c4e522a
https://dockyard.com/blog/2017/08/15/elixir-tips