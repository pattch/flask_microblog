SpaceX Programming Test
=======================

The goal of the SpaceX programming test is to evaluate the programming abilities
of candidates. The ideal candidate would know Python, JavaScript, and/or Go (or
another language with great proficiency), be familiar with basic database and
HTTP API principles, and able to write clean, tested, and maintainable code.
This test gives candidates a chance to show these abilities.

Taking the Test
---------------

You have five hours to implement your solution. The test will be administered
through email. At the beginning of the test, the test proctor will send you the
problem description via email. Your solutions will be submitted back to the
proctor via email.

The test will involve implementing a database-backed service, and the proctor
will run your service against a validation suite to ensure it meets all
requirements.

Even though you should not use the proctor as a test engineer, you may provide
early submissions. If your submission fails some of the tests and if there is
time remaining, the proctor will attempt to give you feedback so that you can
fix your program and resubmit.

It's highly recommended to make at least one submission very early in the test
(once you have figured out the basic structure of your application, how to
install any needed dependencies and how to boot your application) so the proctor
can verify your submission starts up without errors at SpaceX. Doing this early
on in the testing process will help get you quick feedback towards the end.

Getting Your Environment Ready
------------------------------

You'll need a computer to work on and email access. You'll also need to set up
Docker CE (https://www.docker.com/community-edition), which is free. Sample
`Dockerfile` and `docker-compose.yml` files are included here for you to test
your setup.

Please make sure you can bring up your app with `docker-compose up --build` well
before the start of the test. You should be able to browse http://localhost:9090
if the basic setup works.

To save time, we also suggest updating the `Dockerfile` and/or adding services
to `docker-compose.yml` to gain access to any tools (databases you're familiar
with, your favorite Python, Javascript, Go, or Ruby packages, etc.) you think
you might need ahead of time so you don't lose valuable time during the test.

When you make a submission, we will `docker-compose up --build` your app from a
machine connected to the internet and expect a fully functioning service without
manual intervention from the proctor's side.

Questions and Clarifications
----------------------------

If the rules of the test or the description of the problems seem unclear or need
clarification, please ask. Since part of the point of the test is to interpret
the specification and solve the problem, we may not answer all questions, but if
our descriptions are unclear or sent you down the wrong path, we may be able to
save you from wasting precious time.

Extra Credit
------------

If you are supplied with a problem which describes some of its components as
optional, do not assume that you have to implement any of them. We often include
more options than can be completed in the allotted time even by fast
programmers. A solid solution to the core problem is much more important than
any solution to the optional components. Even a perfect solution on an optional
component will not make up for a poor solution to the core problem. Budget your
time accordingly.

Evaluation Criteria
-------------------

When evaluating the program, the following are among the factors considered:

 * Does it run?
 * Does it produce the correct output?
 * How did _you_ gain confidence your submission is correct?
 * Were appropriate algorithms and data structures chosen?
 * Was it well written? Are the source code and algorithms implemented cleanly?
   Would we enjoy your code living along side our own?
 * Is it slow? For small to medium sized inputs, the processing delay should
   probably not be noticeable. For a computer which is not particularly fast,
   spending a few seconds is fine. Spending minutes on large inputs is probably
   bad.

As mentioned above, a solid, well-tested solution to the core problem is more
important than any solution to any optional components of the problem.

