Now we're getting to the fun stuff. In lesson 3, we will define our first meaningful neural network and will apply it to an interesting use case. Let's start by describing the use case.

You take tests all the time. Sometimes you study and do well. Other times, you procrastinate and stay up late the night before the test to cram. You've probably heard the advice that you should get a good night's rest before an exam, but you're still unsure that it's the best course of action. Equipped with your new machine learning skills, you set out to find out the optimal amount of studying and sleeping you should do. Once you build a model, you can use the results to make better decisions and improve your time management.

The first thing you need to do is gather some data. So for the next couple of weeks, you log the total number of hours studied for each test and the number of hours you slept the night before the test. Your data looks like this:

```bash
 hours studied  |  hours slept  |  test score
---------------------------------------------
       10       |      7        |     97
        5       |      4        |     71
        8       |      3        |     74
        2       |      8        |     78
        4       |      8        |     90
        9       |      1        |     68
        6       |      8        |     95
        1       |      7        |     65
        5       |      3        |     70
        7       |      6        |     82
---------------------------------------------
```