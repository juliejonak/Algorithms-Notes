# How to Write and Analyze Algorithms Notes

##### What is the difference between an algorithm and a function? 

An algorithm is just a little more general than a function. An algorithm is a set of steps to solve some problem, whereas a function is a set of specific steps to solve a specific problem.

"A function is concrete, and does have a machine implementation. In computer programming, a function is an implementation of an algorithm. An algorithm is a series of steps (a process) for performing a calculation, whereas a function is the mathematical relationship between parameters and results." - Google.

##### Abstraction

Abstraction is when we lessen the details/information, or when we use something without knowing how it works in detail.

We use algorithms all the time as an abstracted version of an implementable function.

There are sets of steps we do daily - tie our shoes, drive to work - that are abstracted out. We aren't focusing on each specific step and way that those things work mechanically.

Algorithms are known as mathematical and complicated ideas, which they can be, but also are not inherently.

Instead of trying to solve a problem we encounter specifically, this week we want to focus on how to solve problems generally in writing applications, by following a general set of steps:

#### POLYA Problem Solving Technique

This is a four step problem solving process you can use to identify problems and come up with a solution.

See in depth POLYA explanation: https://math.berkeley.edu/~gmelvin/polya.pdf

The common steps are....

#### 1. Understand the Problem

This means making sure you're solving what is actually being asked to be solved. If we misunderstand the problem, we might create a viable solution for _a_ problem, but not the correct problem.

Ask questions and ensure you have a solid understanding of the problem before beginning any following steps.

*"Can I assume that..."*

Like, "Can I assume that the user will only input valid numerical data or do I need to assume they can input anything?"

Spending the time up front to fully understand what needs to be done, next you should...

#### 2. Come Up With a Plan (Pseudo-code)

Don't just jump into coding. It's far more efficient to pause and come up with a plan.

As you write a gameplan or a few lines of pseudo-code, you'll often come up with additional ideas, edge cases, potential difficulties, etc.

Then...

#### 3. Code Your Solution

Execute your game plan to get to a working solution - a first pass solution. It might not be elegant or optimized. You just want to get to an MVP solution.

Afterwards, you can analyze it for an optimized solution, time permitting.

The most important thing is to get it working, even if in a brute force manner.

#### 4. Analyze and Optimize 

During this step is a good time to find edge cases or ways that you would optimize your solution, expressing the logic behind those to your interviewer.

Consider addressing issues of scalability or unusual cases. Refactor for cleaner code.



##### What if we don't understand the problem?

If there is a term being used that you are unfamiliar with - ask about it. In an interview situation, most hiring managers should clarify and appreciate you taking the time to fully understand the problem.

Identify exactly what you are being asked to return or show - what is the end result being returned from a good solution? Is is a numerical value? A string?

What are the inputs being given? What kind of data should I expect to be given?

A good way to verify you understand the problem is by rephrasing and summarizing it back to them: "From my understanding, what we're trying to do is..."

Draw a diagram or picture to help fully understand the problem. You can draw a visual example, a diagram of how the data flows, create a small mathematical example, the recursive call stack to identify the base case, etc.


##### Is it common to calculate Big O in an interview?

It depends on the industry and company - if that's important to them - but being able to look at something and give a rough example of the run time is an important skill.

It can also simply be a bonus to an interviewer to show that beyond being able to solve problems, you care about and understand optimization.


#### Factorials

_See file algs.py for the code to this section:_

A factorial is when something is the product of an integer and all the integers below it.

I.e. 4! = 4 * 3 * 2 * 1

What are some questions we might ask about writing a function that returns the factorial of the given number, using an iterative approach (not recursion)?

- What are the expected inputs? Are they positive integers?
- What is considered 0!? (Possible edge case)
- Are there any upper limits?
- Are any string being input?
- What should be returned from this function?

Once we have these assumptions answered, we'll make a plan. A good method is outlining our plan as comments within the code.

If we think about a base case, what is the _last_ number we multiply? 1.

Thinking about that, we'll do something _until_ something is 1. This implies a loop.

Within that loop, we need to multiply.

We'll initialize our returned result as 1 because even if the integer given is 0, it'll return one.

Our plan looks like:

def iter_factorial(n):

```
    result = 1
    # loop until 1
        # multiply
    
    return result
```

When we fill this in, it looks like...

```
def iter_factorial(n):
    result = 1
    # loop until 1
    while n > 1:
        # multiply
        result *= n
        n -= 1
    
    return result

n = 4
print('Result when n is', n, 'is: ', iter_factorial(n))
```

##### What would be the run time of this function?

Result and the return statement will only run once, no matter how large n is.

But the loop will run depend on how large n is. It will run n-1 times.

Remember though, we drop associated integers when evaluating run time so this would reduce down to O(n) or linear time.

See these notes for a better break down on run time of Big O: https://github.com/juliejonak/Algorithms-I-Notes

Remember:

#### The 3 main rules of Big O

```
1. Discard the constant
2. The bigger Big O Notation dominates (less efficient wins)
3. We're interested in what happens with large values of `n` 
because some processes can be deceptively efficient with small 
values, but that doesn't account for scalability.
```










