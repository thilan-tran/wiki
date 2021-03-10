---
#YAML Frontmatter
title: "Philosophy 31: Symbolic Logic"
subtitle: "Professor Levy"
date: "Winter 2021"
author: "Thilan Tran"
mainfont: Libertinus Serif
monofont: Iosevka
fontsize: 14pt
toc: true
documentclass: extarticle
header-includes: |
  \definecolor{Light}{HTML}{F4F4F4}
  \let\oldtexttt\texttt
  \renewcommand{\texttt}[1]{
    \colorbox{Light}{\oldtexttt{#1}}
  }
  \usepackage{fancyhdr}
  \pagestyle{fancy}
---

\newpage{}

# Philosophy 31: Symbolic Logic
***

# Logical Language
***

- in logic, an **argument** is a set of sentences:
  - one of which is designated as a **conclusion**
  - the other sentences are called **premises**

- ex. argument:
  1. All dogs are animals.
  2. Some animals are pigs.
  3. Therefore some dogs are pigs.
  - (1) and (2) are premises, (3) is the conclusion of the argument:
    - argument is often signaled by *indicator* words eg. "therefore", "hence", "thus"
    - while premises are signaled by "because", "since", etc.

- an argument is **valid** if it is impossible for the premises to all be true and the conclusion false:
  - ie. if the premises are all true, then the conclusion must be true
    - the example argument is a *valid* argument!
  - at least, in deductive logic
    - in inductive reasoning, premises *lend support* to a conclusion
  - note that the validity of an argument has to do with its inherent logical structure
    - can replace the parts of the argument uniformly and the argument would remain valid

- an argument is **sound** if it is valid and all of its premises are true:
  - the example argument is valid, but not sound
  - note that a sound argument *must* be valid

- ex. argument:
  1. If John eats pizza he will get thirsty.
  2. If John eats pasta he will get thirsty.
  - valid argument

- ex. argument:
  1. If John eats pizza he will get thirsty.
  2. John got thirsty therefore John ate pizza.
  - *invalid* argument

- ex. argument:
  1. If John eats pizza he will get thirsty.
  2. If John does not eat pizza he will be hungry.
  3. If John will not get sick he will not be hungry.
  4. Therefore John will get sick.
  - valid argument!

- a set of sentences **implies** a given sentence if and only if the truth of the given sentence is *gauranteed* by the truth of all members of the set
  - ie. sentence A implies another sentence B if and only if A's truth guarantees B's
  - eg.
    1. Peter likes pizza and Patsy likes pasta.
    2. Patsy likes pasta.
    - sentence (1) implies sentence (2)

- sentence A is **equivalent** to sentence B if and only if A and B always agree in truth value
  - eg.
    1. No dogs are cats.
    2. No cats are dogs.
    - equivalent sentence
  - eg.
    1. Either Peter likes pizza or Patsy likes pasta.
    2. Peter likes pizza.
    - not equivalent

## Symbolic Language
***

- to analyze the validity of an argument:
  1. *extract* the logical structure of an argument
      - by translating into a representative **symbolic language**
  2. *generally* analyze that structure

### Vocabulary

- vocabulary:
  - predicate letters are $A, \ldots, O$
  - name letters are $a, \ldots, h$
  - variables are $i, \ldots, z$
  - universal quantifier $\forall$
  - existential quantifier $\exists$
  - sentence letters are $P, \dots, Z$
    - with or without subscripts
  - sentential connectives:
    - $\land$ ie. "and", $\lor$ ie. "or", $\to$ ie. "if-then", $\leftrightarrow$ ie. "if and only if"
    - ${\sim}$ ie. "it is not the case that"
  - punctuation is parantheses

- ex. Peter loves pizza.
  - this is an **atomic sentence** that cannot be broken up further
- ex. Peter loves pizza because Patsy does.
  - this is a **compound** sentence since it is connected by the **binary connective** "because"

- in logic, we are only concerned with **truth functional connectives**:
  -  a connective is truth functional if and only if the truth values of the joined sentences always completely determine the truth value of the compound sentence
  - eg. "and", "or", "then", "if and only if" are binary truth functional connectives
  - eg. "it is not the case" ie. a negation operator is a *unary* truth functional connective

- ex. Peter loves pizza because Patsy makes pizza.
  - if we know the truth value of each component, can we determine the truth value of the compound sentence?
  - no, "because" is *not* a truth functional connective

### Grammar

- in a **metalanguage**, sentences talk about a language itself
  - eg. "John" is tall vs. John is tall.

- recursive symbolic language grammar rules:
  1. sentence letter is a symbolic sentence
  2. a symbolic sentence preceded by a ${\sim}$ is a symbolic sentence
  3. if a binary connective is placed between two symbolic sentences and enclosed in parentheses, the result is a symbolic sentence
  - eg. $P, Q, (P \to Q), {\sim} P, ({\sim} P\leftrightarrow(P\to Q))$ are all symbolic sentences
  - informal conventions:
    1. outermost parentheses may be omitted
    2. conditionals and biconditionals are assumed to *outrank* conjunctions and disjunctions:
        - thus parentheses may be omitted around conjunctions and disjunctions when there is no ambiguity
        - eg. note that a reduction like $P \lor Q \land R$ is ambiguious
    3. allow brackets and braces
    - by convention, we restore parentheses to the left when we have a string of the same connectives

- an **atomic sentence** is a symbolic sentence containing no connectives
- a **molecular sentence** is a symbolic sentence with one more connectives
- a **negation** is any sentence of the form ${\sim} \square$
- a **conditional** is any sentence of the form $(\square \to \bigcirc)$:
  - $\square$ is the **antecedent**
  - $\bigcirc$ is the **consequent**
- a **conjunction** is any sentence of the form $(\square \land \bigcirc)$
- a **disjunction** is any sentence of the form $(\square \lor \bigcirc)$
- a **biconditional** is any sentence of the form $(\square \leftrightarrow \bigcirc)$

- the **scope** of a connective is the connective itself with the components and grouping indicators it links together:
  - ie. what the connective applies to
  - eg. in $((P\land {\sim} Q) \to R)$, ${\sim}$ has a scope of ${\sim} Q$, $\land$ has a scope of $(P\land {\sim} Q)$, $\to$ has a scope of the entire formula ie. sentence
  - the **main connective** is the connective occurence with the largest scope
    - always ranges over entire formula

- additional constructs used with quantifiers:
    - a **quantifier phrase** is a quantifier followed by a variable
    - **terms** are all lowercase letters ie. name letters and variables
    - **atomic formulas** are sentence letters or predicate letters followed by a term:
        - can't logically break these down
        - all atomic sentences are atomic formulas
    - **molecular formulas** are atomic formulas connected by binary connectives
    - **quantified formulas** are constructed from a quantifier phrase and a formula:
        - if the main connective is a universal quantifier, we have a **universal generalization** eg. $\forall x \square$
        - if the main connective is a existential quantifier, we have an **existential generalization** eg. $\exists x \square$

\newpage{}

# Symbolization
***

| $\square$ | ${\sim}\square$ |
|-----------|-----------------|
| T | F |
| F | T |
Table: Truth Table for ${\sim}P$

| $\square$ | $\bigcirc$ | ${\sim}\square$ | $\square\to\bigcirc$ | $\square\land\bigcirc$ | $\square\lor\bigcirc$ | $\square\leftrightarrow\bigcirc$ |
|-----------|------------|-----------------|----------------------|------------------------|-----------------------|----------------------------------|
| T | T | F | T | T | T | T |
| T | F | F | F | F | T | F |
| F | T | T | T | F | T | F |
| F | F | T | T | F | F | T |
Table: Truth Table for Binary Connectives

- to perform **symbolization** ie. convert English sentences to their symbolic equivalents:
  1. make a scheme of abbreviation
      - in doing so, make all the sentences positive
  2. rewrite the sentences replacing atomic components with sentence letters
  3. group
  4. replace the connectives with symbols
  - watch for stylistic variants and hidden negations in sentences

- ex. If Herbie eats pizza, then Herbie gets sick.
  - equivalent sentences:
    - Provided that Herbie eats pizza, he will get sick.
    - Herbie gets sick if he eats pizza.
  - other equivalent stylistic variants:
    - "if", "provided that", "given that", "in case", "in which case", "assuming that", "on the condition that"
  - $P:$ Herbie eats pizza, $Q:$ Herbie gets sick
  - If P, then Q.
  - $P \to Q$

- ex. The patient will live only if we operate.
  - $P:$ the patient lives, $Q:$ we operate
  - P only if Q.
  - $P \to Q$

- ex. Bruce likes Budweiser, Miller, and Heineken.
  - $P:$ Bruce likes Budweiser, $Q:$ Bruce likes Miller, $R:$ Bruce likes Heineken
  - this is known as **telescoping** of conjunctions and disjunctions
  - $(P \land Q) \land R$

- ex. Peter likes pizza but not pasta.
  - one of several other stylistic variants for "and":
    - "but", "although", "as well", *commas*
  - $P \land {\sim} Q$

- ex. Peter brings his lunch unless the cafeteria is open.
  - ex. The patient will die unless we operate.
  - "unless" is a stylistic variant for "or"
  - "or" and its variants is considered *inclusive* unless otherwise specified
  - $P \lor Q$

- ex. Neither Peter nor Patsy came to the party.
  - ${\sim}P \land {\sim}Q = {\sim}(P \lor Q)$

- ex. If Herbie eats pizza at night or drinks cheap beer,
then only if his girlfriend stays with him, will he have nightmares.
  - $P:$ Herbie eats pizza, $Q:$ Herbie drinks beer, $R:$ girlfriend stays, $S:$ Herbie has nightmares
  - $(P \lor Q) \to (S \to R)$

- more variations:
  - ex. If Herbie's girlfriend stays with him, then he will not have nightmares although he drinks cheap beer.
    - $R \to ({\sim}S \land Q)$
  - ex. If Herbie eats pizza at night, he will have nightmares unless he drinks cheap beer.
    - $P \to (S \lor Q)$

- ex. You may have ice cream or cotton candy.
  - considered inclusive by default
  - ex. You may have ice cream or cotton candy, but not both.
    - forces an exclusive-or
    - $(P \lor Q) \land {\sim}(P \land Q) = P \leftrightarrow ~Q$

- ex. Ruth studies hard unless she's tired, in which case she doesn't.
  - "unless" indicates "or", the comma indicates an "and", and the "in which case" indicates an "if-then"
  - $(S \lor T) \land (T \to {\sim}S)$

- ex. If Alfred and Mary are playing dice together, it is the first throw of the game, and Mary is throwing the dice, then she wins the game on the first throw if and only if she throws 7 or 11.
  - $P:$ Alfred plays, $Q:$ Mary plans, $R:$ Alfred and Mary play, $S:$ is first throw
  - $T:$ Mary is throwing, $U:$ Mary wins on first throw, $V:$ Mary throws 7 or 11, $W:$ Mary throws 7, $X:$ Mary throws 11
  - $R \land S \land T \to (U \leftrightarrow W \lor X)$
    - break down atomic structure when possible
    - note that $R$ is not equivalent to $P \land Q$
  - another way to express "if and only if" is "precisely if" and "just in case"

- ex. Assuming either that logic is difficult or that the text is not readable, Alfred will pass only if he concentrates.
  - $P:$ logic is difficult, $Q:$ text is readable, $R:$ Alfred will pass, $Q:$ Alfred concentrates
  - $(P \lor {\sim}Q) \to (R \to S)$

- ex. Assuming the professor is a Communist, he will sign the oath; but if he is an idealist, he will neither sign the oath nor speak to those who do.
  - $(P \to Q) \land (R \to {\sim}(Q \lor S))$

- ex. Among USC, UCLA, Oregon, and Arizona, exactly two will be in contention in November.
    - need to list out all the possible combinations
    - note that to specify two, we need to "and" those while negating the remaining ones

- symbolizing an entire argument with truth values in \ref{truths}:
  - If Herbie eats pizza, then he will get sick.
  - If Herbie does not eat pizza, then he will be hungry.
  - If Herbie will not get sick, then he will not be hungry.
  - Therefore Herbie will get sick.
  - $P:$ Herbie eats pizza, $Q:$ Herbie gets sick, $R:$ Herbie will be hungry
  - note that it is impossible for all the premises to be true and the conclusion false:
    - thus this argument is valid
    - if there were a case where all the premises are true and the conlusion false, the argument would be invalid

| P | Q | R | $P\to Q$ | ${\sim}Q\to R$ | ${\sim}Q\to {\sim}R$ | $\therefore Q$ |
|---|---|---|----------|----------------|----------------------|----------------|
| T | T | T | T        | T              | T                    | T              |
| T | T | F | T        | T              | T                    | T              |
| T | F | T | F        | T              | F                    | F              |
| T | F | F | F        | T              | T                    | F              |
| F | T | T | T        | T              | T                    | T              |
| F | T | F | T        | F              | T                    | T              |
| F | F | T | T        | T              | F                    | F              |
| F | F | F | T        | F              | T                    | F              |
Table: Truth Values of an Example Argument \label{truths}

- categorizing sentences:
  - a **tautology** is a symbolic sentence that is always true
  - an **impossible** symbolic sentence is always false
  - otherwise, the sentence is **contingent**
  - if two sentences have the same truth table, they are **logically equivalent**
    - putting a biconditional between two logically equivalent sentences makes a tautology

## Quantifiers
***

- ex. Socrates is a man.
    - $F:$ $\{1\}$ is a man, $a:$ Socrates
        - $F$ is a 1-place predicate ie. with a single placeholder
    - $Fa$

- ex. Something is missing.
    - $G:$ $\{1\}$ is missing
    - $\exists xGx$

- ex. Everything is wonderful.
    - $H:$ ${\{1\}}$ is wonderful
    - $\forall xHx$

- ex. All men are mortal.
    - $F: \{1\}$ is a man, $G: \{1\}$ is mortal
    - $\forall  x(Fx \to Gx)$
        - limiting the domain of discourse

- ex. Some students are annoying.
    - $F: \{1\}$ is a student, $G: \{1\}$ is annoying
    - $\exists x(Fx \to Gx)$ is incorrect!
    - $\exists x(Fx \land Gx)$

- a quantifier phrase will bind a variable if:
    - the variable is within the scope of the quantifier phrase
    - the variable has to be the same as the one occurring in the quantifier phrase
    - the variable cannot be already bound
    - eg. in $\forall x(Fx \to Gx)$, both $x$ bind to the same $x$
    - eg. in $\forall xFx \to \forall xGx$, the $x$'s on either side of the implication are different
    - eg. in $\forall x(Fx \to \exists y(Gy \lor Fx))$, the $x$'s bind to the same $x$ and the $y$ binds to the only $y$
    - eg. in $\exists \forall y(Fx \to (\forall x(Gy \land Hx) \land Gx))$:
        - the innermost $x$ binds to its closest $x$
        - the $y$ binds to the only $y$
        - the remaining $x$'s bind to the very first $x$
    - eg. in $\exists x \exists y (Fx \to (\forall yGy \lor Hy) \land Ix) \lor \exists y (Fy \lor Hx)$:
        - all variables are bound *except* for the very last $x$
        - in a **symbolic sentence** all variables are bound
        - this is a **symbolic formula** since it has a free variable, but is otherwise well formed
        - when symbolizing an English sentence, it should result in a symbolic sentence

- ex. Symbolize the following sentences given that $F: \{1\}$ is a logic student and $G: \{1\}$ is cool:
    - All logic students are cool.
        - $\forall x(Fx \to Gx)$
        - same symbolization for "logic students are cool", which has an implied "all".
    - Some logic students are cool.
        - $\exists x(Fx \land Gx)$
    - No logic student is cool.
        - $\forall x(Fx \to {\sim}Gx)$
        - equivalently, ${\sim}\exists(Fx \land Gx)$
    - Only logic students are cool.
        - $\forall x(Gx \to Fx)$

- ex. Symbolize the following sentences given that $F:\{1\}:$ is an even number, $G: \{1\}$: is a prime number, $H: \{1\}$ is honest, $J: \{1\}$ is a person, $a:$ 2, $b:$ 4, and $c:$ Abraham Lincoln:
    - If anyone is honest, then Abraham Lincoln is honest.
        - "any" can mean "all" or "some" in different contexts
        - in this case, "any" indicates "some"
        - $\exists x(Jx\land Hx) \to Hc$
        - equivalently, $\forall x (Jx \land Hx \to Hc)$
    - If 2 is a prime number, then there is an even prime number.
        - $Ga \to \exists x(Fx \land Gx)$
    - 4 is a prime number if and only if all even numbers are prime numbers.
        - $Gb \leftrightarrow \forall x(Fx \to Gx)$
    - If there is an even prime number, then there is an even number and there is a prime number.
        - $\exists (Fx \land Gx) \to \exists xFx \land \exists xGx$
        - note the existential quantifier does not distribute across parentheses
    - If 4 is a prime number and there is an even number, then there is an even prime number.
        - $Gb \land \exists xFx \to \exists x(Fx\land Gx)$

- ex. Men and women over 18 are permitted to vote.
    - $F: \{1\}$ is a man, $G: \{1\}:$ is a woman, $H: \{1\}:$ is over 18, and $J: \{1\}:$ is permitted to vote
    - $\forall x((Fx \lor Gx) \land Hx \to Jx)$
    - equivalently, $\forall x (Fx \land Hx \to Jx) \land \forall x (Gx \land Hx \to Jx)$

- ex. Only citizens can vote.
    - $F: \{1\}$ is a citizen, $G: \{1\}$ can vote
    - $\forall x(Gx \to Fx)$

- ex. If everything is mental, then nothing is physical unless something is both mental and physical.
    - $F: \{1\}$ is mental, $G: \{1\}$ is physial
    - $(\forall xFx \to ({\sim}\exists xGx \lor \exists x(Fx \land Gx)))$
        - ${\sim}\exists xGx$ is equivalent to $\forall x {\sim}Gx$

- ex. If those who believe in God have immortal souls, then, given that God exists, they will have eternal bliss.
    - $F: \{1\}$ believes in God, $G: \{1\}$ has an immortal sou, $H: \{1\}$ will have eternal bliss, $P:$ God exists
    - $(\forall x(Fx\to Gx) \to (P \to \forall x(Fx\to Hx)))$
    - equivalently, $\exists x \forall y ((Fx \to Gx)\to (P \to (Fy \to Hy)))$

- ex. All fruits and vegetables are wholesome and nourishing.
    - $F: \{1\}$ is a fruit, $G: \{1\}$ is a vegetable, $H: \{1\}$ is wholesome, $J: \{1\}$ is nourishing
    - $\forall x ((Fx \lor Gx) \to (Hx \land Jx))$
        - fruits *or* vegetables

- ex. If any woman studies, then no student passes unless she does.
    - $F: \{1\}$ is a woman, $G: \{1\}$ studies, $H: \{1\}$ is a student, $J: \{1\}$ passes
    - $\forall x ((Fx \land Gx) \to (\forall y (Hy \to {\sim}Jy) \lor Jx))$
        - $\forall y (Hy \to {\sim}Jy)$ is equivalent to ${\sim}\exists y (Hy \land Jy)$

- ex. Dogs and dolphins jump only if petted.
    - $F: \{1\}$ jumps, $I: \{1\}$ is a dog, $H: \{1\}$ is petted, $K: \{1\}$ is a dolphin
    - $\forall x((Ix \lor Kx) \to (Fx \to Hx))$

- ex. Dogs and dolphins jump only if Spot and Kiwi jump.
    - $F: \{1\}$ jumps, $I: \{1\}$ is a dog, $K: \{1\}$ is a dolphin, $a:$ Spot, $b:$ Kiwi
    - $\forall x((Ix \lor Kx) \to (Fx \to Fa \land Fb))$

\newpage{}

# Derivations
***

- in a valid argument. if the premises are true. then the conclusion must be true:
  - instead of using large truth tables, we can use **natural deduction** to show that arguments are valid
  - uses **derivations** ie. proofs that are composed of lines, each of which is justified by a rule in our system
    - attempts to prove a conclusion

- a derivation has three columns:
  1. line numbers
  2. formula
  3. justification

- three types of proofs:
  1. direct: "Show: P. ... P."
  2. conditional: "Show: P $\to$ Q. P. ... Q."
      - hinges on an assumption P to prove Q
  3. indirect: "Show: P. ~P. ... {contradiction} P."
      - finds an impossibility to show an assumption is wrong

- ex. A direct derivation:
  1. ~~Show~~: Mustard is the murderer.
  2. Scarlet was in the billiard room.
  3. If Scarlet was in the billiard room, then the rope isn't in the study.
  4. So the rope isn't in the study.
  5. Either the rope is in the study or Plum didn't do it.
  6. So Plum didn't do it.
  7. If Plum didn't do it, then Mustard is the murderer.
  8. So Mustard is the murderer.

- ex. A direct derivation for the following symbolic argument:
  - $S, T \lor {\sim}P, {\sim}P \to R, S \to {\sim}T, \therefore R$
  1. ~~Show~~: $R$
  2. $S$ | Premise
  3. $S \to {\sim}T$ | Premise
  4. ${\sim}T$ | 2, 3
  5. $T \lor {\sim}P$ | Premise
  6. ${\sim}P$ | 4, 5
  7. ${\sim}P \to R$ | Premise
  8. $R$ | 6, 7
  9. 8 is what we want to show.

- ex. A conditional derivation for the following symbolic argument:
  - $Q \to S, S \to R, R \to T, T \to P, \therefore Q \to P$
  1. ~~Show~~: $Q \to P$
  2. $Q$ | Assume
  3. $Q \to S$ | Premise
  4. $S$ | 2, 3
  5. $S \to R$ | Premise
  6. $R$ | 4, 5
  7. $R \to T$ | Premise
  8. $T$ | 6, 7
  9. $T \to P$ | Premise
  10. $P$ | 8, 9
  11. 10, consequent follows

- ex. An indirect derivation for the following symbolic argument:
  - ${\sim}P \to Q, Q \to R, R \to {\sim}S, S \lor {\sim}Q, \therefore P$
  1. ~~Show~~: $P$
  2. ${\sim}P$ | Assumption
  3. ${\sim}P \to Q$ | Premise
  4. $Q$ | 2, 3
  5. $Q \to R$ | Premise
  6. $R$ | 4, 5
  7. $R \to {\sim}S$ | Premise
  8. ${\sim}S$ | 6, 7
  9. $S \lor {\sim}Q$ | Premise
  10. ${\sim}Q$ | 8, 9
  11. 4 and 10 contradict

## Inference Rules
***

- 10 **inference rules** will be used to justify lines in our derivations

1. Repetition (R): $\square, \enskip \therefore \enskip \square$
    - ie. we can repeat a line in the derivation

2. Double Negation (DN): $\square, \enskip \therefore \enskip {\sim}{\sim}\square$
    - alternatively, \enskip ${\sim}{\sim}\square, \enskip \therefore \enskip \square$

3. Modus Ponens (MP): $\square \to \bigcirc, \enskip \square, \enskip \therefore \enskip \bigcirc$
    - ie. "method of putting"

4. Modus Tolens (MT): $\square \to \bigcirc, \enskip {\sim}\bigcirc, \enskip \therefore \enskip {\sim}\square$
    - ie. "denying the consequence"

5. Simplification (S): $\square \land \bigcirc, \enskip \therefore \enskip \square$
    - alternatively, $\square \land \bigcirc, \enskip \therefore \enskip \bigcirc$

6. Adjunction (Adj): $\square, \enskip \bigcirc, \enskip \therefore \enskip \square \land \bigcirc$

7. Modus Tolendo Ponens (MTP): $\square \lor \bigcirc, \enskip {\sim}\square, \enskip \therefore \enskip \bigcirc$
    - ie. "method of putting by taking away"
    - alternatively, $\square \lor \bigcirc, \enskip {\sim}\bigcirc, \enskip \therefore \enskip \square$

8. Addition (Add): $\square, \enskip \therefore \enskip \square \lor \bigcirc$
    - alternatively, $\bigcirc, \enskip \therefore \enskip \square \lor \bigcirc$

9. Conditional Biconditional (CB): $\square \to \bigcirc, \enskip \bigcirc \to \square, \enskip \therefore \enskip \square \leftrightarrow \bigcirc$

10. Biconditional Conditional (BC): $\square \leftrightarrow \bigcirc, \enskip \therefore \enskip \square \to \bigcirc, \enskip \therefore \enskip \bigcirc \to \square$

- quantifier inference rules:
    1. Universal Instantiation (UI): $\forall x\square x \enskip \therefore \enskip \square y, \enskip \square a, \enskip \square x,$ etc:
        - ie. what is true of all things is true of any particular thing
        - replace all bound variables with a free variable
        - eg. $\forall x (Fx \to Gx) \enskip \therefore \enskip Fa \to Ga, \enskip Fy \to Gy$
    2. Existential Generalization (EG): $\square a \enskip \therefore \enskip \exists x \square x$:
        - if a particular thing has a property, then something does
        - only have to replace *some* named variables with bound variables
        - eg. $Fa \land Ga \enskip \therefore \enskip \exists x(Fx \land Ga)$
    3. Existential Instantiation (EI): $\exists x \square x \enskip \therefore \enskip \square y, \enskip \square i$, etc:
        - ie. what is true of something is true of a partiular thing
        - note that we cannot instantiate with a specific name letter, must be to a brand new variable that has never occured in the proof
        - eg. $\exists x (Fx \land Gx \enskip \therefore \enskip Fy \land Gy)$

## Formal Derivation Rules
***

- a **derivation** is a sequence of lines that is built up in order, consisting of any of the following provisions:
    - a **show line** consists of the word "Show" followed by a symbolic sentence
        - needs no justifications and can be introduced at any step
    - a **premise** is a symbolic sentence from the given set, justified with the notation "PR"
    - at any step, a line may be introduced if it follows by a rule from sentences on the previous available lines:
        - justified by citing the numbers of previous lines and the rule name
        - an available line is not preceded by a "Show" and not boxed
    - in a **direct derivation**, when a line whose sentence is the same as the closest uncancelled show line:
        - write "DD" following the justification for that line
        - draw a line through "Show"
        - draw a box around all lines below the show line, including the current line
    - as an **assumption for conditional derivation**, when a show line with a conditional sentence is introduced, the following line can be introduced with the antecedent of the conditional and justification "ASS CD"
    - in a **conditional derivation**, when a line whose sentence is the same as the consequent of closest uncancelled show line:
        - write "CD" following the justification for that line
        - draw a line through "Show"
        - draw a box around all lines below the show line, including the current line
    - as an **assumption for indirect derivation**, when a show line is introduced, the following line can be introduced with the negation of the sentence on the show line and justification "ASS ID"
    - in an **indirect derivation**, when a line whose sentence is the negation of a previous available line is introduced:
        - write "DD" following the justification for that line, with the line number of the contradicted sentence
        - draw a line through "Show"
        - draw a box around all lines below the show line, including the current line

- in a **universal derivation**, want to show something of the form $\forall x \square x$:
    - proving for any particular thing can be proved for anything
    - just have to show $\square x$
        - as long as $x$ does not occur free on any available line in the derivation prior to the "Show" line

## Derivation Strategies
***

1. to get started:
    - to show a conditional, assume the antecedent and show the consequent
    - to show a conjunction, first show one conjunct, then the other, then use Adj. to put them together for a direct derivation
    - to show a biconditional, first show the conditional in one direction and then the other to use CB to put them together for a direct derivation
    - to show anything else, begin an indirect derivation by assuming its negation

2. look for ways to break down available lines using MP, MT, S, MTP, BC
    - may need to use DN on an available line first

3. if one of the lines is the negation of the conditional, show the conditional itself to generate a contradiction

4. if one line is the negation of a disjunction, see if you can use Add. with another line to get the disjunction itself to generate a contradiction

5. look for remaining conditionals and disjunctions that have not yet been broken:
    - for any conditionals, show either:
        - the antecedent to use MP to break it down
        - the negation of the consequent to use MT to break it down
    - for any disjunction, show the negation of one of the disjuncts in order to use MTP to break it down

## Examples
***

- ex. Derive ${\sim}P, \enskip Q\to P \enskip \therefore \enskip {\sim}Q$.
```xorg
Show ~Q
~P          PR
Q->P        PR
~Q          2 3 MT
            4 DD
```
- ex. Derive ${\sim}{\sim}(P\to Q), \enskip P \enskip \therefore \enskip Q$.
```xorg
Show Q
~~(P->Q)    PR
P           PR
P->Q        2 DN
Q           3 4 MP
            5 DD
```
- ex. Derive $P, \enskip R \to {\sim}Q, \enskip P \to Q \enskip \therefore \enskip {\sim}R$.
```xorg
Show ~R
P           PR
R->~Q       PR
P->Q        PR
Q           2 4 MP
~~Q         5 DN
~R          3 5 MT
            7 DD
```
- ex. Derive $P \to (Q \to R), \enskip (Q \to R) \to S, \enskip {\sim}S \enskip \therefore \enskip {\sim}P$.
```xorg
Show ~P
P->(Q->R)   PR
(Q->R)->S   PR
~S          PR
~(Q->R)     3 4 MT
~P          2 5 MT
            6 DD
```
- ex. Derive $P \to Q, \enskip Q \to R \enskip \therefore \enskip P \to R$.
```xorg
Show P->R
P           ASS CD
Show R
~R          ASS ID
P->Q        PR
Q->R        PR
~Q          4 6 MT
~P          5 7 MT
P           2 R     # need to repeat line so it becomes available for deriv. rule
            8 9 id
            3 CD
```
Alternatively:
```xorg
Show P->R
P           ASS CD
Show R
~R          ASS ID
P->Q        PR
Q->R        PR
Q           2 5 MP
R           6 7 MP
            8 DD    # mixed derivation since we began with an indirect assumption
            3 DD
```
- ex. Derive ${\sim}P\to W \enskip \therefore \enskip (R \to {\sim}W) \to (R\to P)$.
```xorg
Show (R->~W)->(R->P)
R->~W       ASS CD
Show R->P
R           ASS CD
Show P
~P          ASS ID
~P -> W     PR
W           6 7 MP
~W          2 4 MP
            8 9 ID
            5 CD
            3 CD
```
- ex. Derive $(R\to S)\to P, \enskip {\sim}S \to Q \enskip \therefore \enskip {\sim}P \to Q$.
```xorg
Show ~P->Q
~P          ASS CD
Show Q
~Q          ASS ID
(R->S)->P   PR
~S->Q       PR
~~Q         4 6 MT
~(R->S)     2 5 MT
Show R->S
S           7 DN
            10 CD
            8 9 ID
            3 CD
```
- ex. Derive $P\to (Q\to R), \enskip P \to ({\sim}Q \to R), \enskip {\sim}P \to (Q\to R), \enskip {\sim}P \to ({\sim}Q \to R) \enskip \therefore \enskip R$.
```xorg
Show R
~R          ASS ID
P->(Q->R)   PR
P->(~Q->R)  PR
~P->(Q->R)  PR
~P->(~Q->R) PR
Show P # cannot break down further, try assuming ant. of a remaining conditional
~P          ASS ID
Q->R        5 8 MP
~Q->R       6 8 MP
~Q          2 9 MT
~~Q         2 10 MT
            11 12 ID
Q->R        3 7 MP
~Q->R       4 7 MP
~Q          2 14 MT
~~Q         2 15 MT
            16 17 ID
```
- ex. Derive $(P\to Q) \to (T \to R), \enskip U \to {\sim}R, \enskip {\sim}(S\to P) \enskip \therefore \enskip U \to {\sim}T$.
```xorg
Show U->~T
U           ASS CD
Show ~T
T           ASS ID
(P->Q)->(T->R) PR
U->~R       PR
~(S->P)     PR
~R          2 6 MP
Show S->P
S           ASS D
Show P
~P          ASS ID
Show P->Q
P           ASS CD
~P          12 R
            14 15 ID
T->R        5 13 MP
R           4 17 MP
~R          8 R
            18 19 ID
            11 CD
            7 9 ID
            3 CD
```
- ex. Derive $\therefore \enskip (P \land Q \to R) \to (P\to(Q\to R))$.
```xorg
Show (P^Q->R)->(P->(Q->R))
P^Q->R      ASS CD
Show P->(Q->R)
P           ASS CD
Show Q->R
Q           ASS CD
Show R
~R          ASS ID
P^Q         4 6 ADJ
R           2 9 MP
            8 10 ID
            7 CD
            5 CD
            3 CD
```
- ex. Derive ${\sim}(R\to T) \enskip \therefore \enskip {\sim}Q\lor T \to R \land {\sim}Q$.
```xorg
Show ~Q+T->R^~Q
~Q+T        ASS CD
Show R^~Q
~(R->T)     PR
Show R
~R          ASS ID
Show R->T
R           ASS CD
~R          6 R
            8 9 ID
            9 CD
~(R->T)     4 R
            7 15 ID
Show ~Q
~~Q         ASS ID
T           2 18 MTP
Show R->T
T           19 R
            21 CD
~(R->T)     4 R
            20 23 ID
R^~Q        5 17 ADJ
            25 DD
            3 CD
```
- ex. Derive $(P\lor Q)\land {\sim}R, \enskip {\sim}R\to(S\land{\sim}P), \enskip Q\to (P\lor T) \enskip\therefore\enskip {\sim}T\to U$
```xorg
Show ~T->U
~T          ASS CD
Show U
~U          ASS ID
(P+Q)^~R    PR
~R->S^~P    PR
Q->P+T      PR
P+Q         5 S
~R          5 S
S^~P        6 9 MP
S           10 S
~P          10 S
Q           8 12 MTP
P+T         7 13 MP
P           2 14 MTP
            12 15 ID
            3 CD
```
- ex. Derive $(P\to Q)\land (R\to P), \enskip (P\lor R)\land {\sim}(Q\land R) \enskip\therefore\enskip (P\land Q)\land {\sim}R$.
```xorg
Show P^Q^~R
(P->Q)^(R->P)   PR
(P+R)^~(Q^R)    PR
Show P^Q
Show P
~P              ASS ID
P->Q            2 SL
R->P            2 SR
P+R             3 SL
~(Q^R)          3 SR
~R              6 8 MT
P               9 11 MTP
                6 12 ID
Show Q
~Q              ASS ID
P->Q            2 SL
~P              15 16 MT
P               5 R
                17 18 ID
P^Q             5 14 ADJ
                20 DD
Show ~R
R               ASS ID
~(Q^R)          3 SR
Q               4 SR
Q^R             25 23 ADJ
                24 26 ID
P^Q^~R          4 22 ADJ
                28 DD
```
- ex. Derive $(P\leftrightarrow {\sim}Q)\to R\enskip\therefore\enskip {\sim}R\land P\to Q$.
```xorg
Show ~R^P->Q
~R^P        ASS CD
Show Q
~Q          ASS ID
(P<->~Q)->R PR
~R          2 SL
P           2 SR
Show P<->~Q
Show P->~Q
~Q          4 R
            10 CD
Show ~Q->P
P           7 R
            13 CD
P<->~Q      9 12 CB
            15 dd
R           5 8 MP
            6 17 ID
            3 CD
```
- ex. Derive ${\sim}Q\to R, \enskip Q\leftrightarrow {\sim}(Q\land R) \enskip\therefore\enskip {\sim}R\leftrightarrow Q$.
```xorg
Show ~R<->Q
~Q->R       PR
Q<->~(Q^R)  PR
Show ~R->Q
~R          ASS CD
Show Q
~Q          ASS ID
R           2 7 MP
~R          5 R
            8 9 ID
            6 CD
Show Q->~R
Q           ASS CD
Show ~R
Q->~(Q^R)   3 BC
~(Q^R)      13 16 MP
Q^R         13 15 ADJ
            17 18 ID
            14 cd
~R<->Q      4 12 CB
            21 DD
```
## Examples with Quantifiers
***

- ex. Derive $\exists xFx, \enskip \forall x(Fx \to Gx) \enskip \therefore \enskip \exists xGx$.
```xorg
Show ?xGx.
~?xGx       ASS ID
?xFx        PR
/x(Fx->Gx)  PR
Fi->Gi      4 UI
Fi          3 EI # *incorrect*, i is not a new variable!
Gi          5 6 MP
?xGx        7 EG
            8 DD

...
Fi          3 EI # need to EI before UI!
Fi->Gi      4 UI
...
```
- `?` indicates $\exists$ and `/` indicates $\forall$

- ex. Derive $\forall x(Fx \to ({\sim}Gx \to Hx)) \enskip \therefore \enskip \forall x(Fx \to Gx \lor Hx)$.
```xorg
Show /x(Fx->Gx+Hx). # can do a UD
Show Fx->Gx+Hx.
Fx          ASS DC
Show Gx+Hx.
~(Gx+Hx)    ASS ID
~Gx^~Hx     5 DM
~Gx         6 SL
~Hx         6 SR
/x(Fx->(~Gx->Hx))   PR
Fx->(~Gx->Hx)       9 UI
~Gx->Hx     3 10 MP
Hx          7 11 MP
            8 12 ID
            4 CD
            2 UD
```
- ex. Derive $\forall x (Fx \lor {\sim}Hx), \enskip \exists x(Hx\land {\sim}Kx), \enskip \forall x(Fx \land {\sim}Kx \to \forall x Jx) \enskip \therefore \enskip \forall xJx$.
```xorg
Show /xJx.
Show Jx.
~Jx         ASS ID
/x(Fx+~Hx)  PR
?x(Hx^~Kx)  PR
/x(Fx^~Kx->/xJx)    PR
Hi^~Ki      5 EI # should always EI before UI
Fi+~Hi      4 UI
Hi          7 SL
Fi          9 DN 8 MTP
Fi^~Ki->/xJx    6 UI
~Ki         7 SR
Fi^~Ki      10 12 ADJ
/xJx        11 13 MP
Jx          14 UI
            3 15 ID
            2 UD
```
- ex. Derive $\forall x(Fx \to Gx), \enskip \forall x(Gx\to Hx) \enskip\therefore\enskip Fa \to \exists x (Gx\land Hx)$.
```xorg
Show Fa->?x(Gx^Hx).
Fa          ASS CD
Show ?x(Gx^Hx).
~?x(Gx^Hx)  ASS ID
/x(Fx->Gx)  PR
/x(Gx->Hx)  PR
Fa->Ga      5 UI
Ga          2 7 MP
Ga->Ha      6 UI
Ha          8 9 MP
Ga^Ha       8 10 ADJ
?x(Gx^Hx)   11 EG
            12 DD
            3 D
```
- ex. Derive $\exists x (Fx\lor Ga), \enskip \forall x(Fx\to Gx) \enskip\therefore\enskip \exists xGx$.
```xorg
Show ?xGx.
~?xGx       ASS ID
?x(Fx+Ga)   PR
/x(Fx->Gx)  PR
Fi+Ga       3 EI
Fi->Gi      4 UI
Show Fi.
~Fi         ASS ID
Ga          5 8 MTP
?xGx        9 EG
~?xGx       2 R
            10 11 ID
Gi          6 7 MP
?xGx        13 EG
            14 DD
```
- ex. Derive $\forall x(Fx\leftrightarrow P), \enskip \exists xFx \enskip\therefore\enskip \forall xFx$.
```xorg
Show /xFx.
Show Fx.
~Fx.        ASS ID
/x(Fx<->P)  PR
?xFx        PR
Fi          5 EI
Fi<->P      4 UI
P           6 7 BP
Fx<->P      4 UI
~P          3 9 BT
            8 10 ID
            2 UD
```
- ex. Derive $\exists x (Fx \land {\sim}Gx)\to\forall x(Fx\to Hx), \enskip \exists x(Fx\land Jx) \enskip\therefore\enskip \forall x(Fx \to {\sim}Hx)\to\exists x(Jx\land Gx)$.
```xorg
Show /x(Fx->~Hx)->?x(Jx^Gx).
/x(Fx->~Hx) ASS DC
Show ?x(Jx^Gx).
~?x(Jx^Gx)  ASS ID
?x(Fx^~Gx)->/x(Fx->Hx)  PR
?x(Fx^Jx)   PR
Fi^Ji       6 EI
Fi          7 SL
Ji          7 SR
Fi->~Hi     2 UI
~Hi         8 10 MP
Show ~Gi.
Gi          ASS ID
Ji^Gi       9 13 ADJ
?x(Jx^Gx)   14 EG
~?x(Jx^Gx)  4 R
            15 16 ID
Fi^~Gi      8 12 ADJ
?x(Fx^~Gx)  18 EG
/x(Fx->Hx)  5 19 MP
Fi->Hi      20 UI
Hi          8 21 MP
            11 22 ID
            3 D
```
## Theorems
***

- some useful theorems:
    - $\therefore \enskip P \to P$
    - $\therefore \enskip Q \to (P \to Q)$
        - ie. if the consequent is true, the conditional is true
    - $\therefore \enskip {\sim}{\sim}P \to P$
        - together with $\therefore \enskip P \to {\sim}{\sim}P$
    - $\therefore \enskip {\sim}P \to (P\to Q)$
        - ie. if antecedent is false, then the conditional is true
    - $\therefore \enskip P \land Q \leftrightarrow Q \land P$ AKA the commutivity of conjunction
    - $\therefore \enskip (P\to Q)\land (Q\to R) \to (P\to R)$ AKA the associativity of conditional
    - $\therefore \enskip {\sim} (P\land {\sim}P)$ AKA law of noncontradiction
    - $\therefore \enskip {\sim}(P\to Q)\leftrightarrow P \land {\sim}Q$ AKA negation of conditional (NC):
        - the negation of a conditional is logically equivalent to antecedent and the negation of the consequent
            - can be seen from the truth table of a conditional
        - very powerful, gives a new derivation rule called NC
    - $\therefore \enskip P \lor Q \leftrightarrow ({\sim}P \to Q)$ AKA the conditional disjunction (CDJ) rule
        - similar to MTP, shows logical equivalence between a disjunction and a similar conditional
    - $\therefore \enskip P \lor {\sim}P$ AKA the law of the excluded middle
    - $\therefore \enskip {\sim}(P\land Q) \leftrightarrow {\sim}P \lor {\sim}Q$ AKA DeMorgan's laws (DM)
        - together with $\therefore \enskip {\sim}(P \lor Q) \leftrightarrow {\sim}P \land {\sim}Q$
    - $\therefore \enskip {\sim}(P\leftrightarrow Q) \leftrightarrow (P \leftrightarrow {\sim}Q)$ AKA negation of biconditonal (NB)

- more useful biconditional theorems:
    - $\therefore \enskip (P\leftrightarrow Q)\land P\to Q$ AKA biconditional ponens (BP)
        - together with $\therefore \enskip (P\leftrightarrow Q) \land Q\to P$
    - $\therefore \enskip (P\leftrightarrow Q)\land {\sim}P\to {\sim}Q$ AKA biconditional tolens (BT)
        - together with $\therefore \enskip (P\leftrightarrow Q) \land {\sim}Q\to {\sim}P$

- useful quantifier negation theorems:
    - $\therefore\enskip \exists x{\sim}\square x \leftrightarrow {\sim}\forall x \square x \enskip$
    - $\therefore\enskip \forall x{\sim}\square x \leftrightarrow {\sim}\exists x \square x \enskip$

- gives us more tools to break down lines:
    - for negations of conditionals, use NC
    - for negations of conjunctions and disjunctions, use DM
    - for negations of biconditonals use NB

- ex. Derive ${\sim}(P\to Q), \enskip {\sim}Q\to R \enskip \therefore\enskip R$ using theorems:
```xorg
Show R
~R          ASS ID
~(P->Q)     PR
~Q->R       PR
~~Q         2 4 MT
P^~Q        3 NC
~Q          6 SR
            5 7 ID
```
- ex. Prove one of DeMorgan's laws, $\therefore \enskip {\sim}(P\lor Q)\leftrightarrow {\sim}P\land{\sim}Q$:
```xorg
Show ~(P+Q)<->~P^~Q
Show ~(P+Q)->~P^~Q
~(P+Q)      ASS CD
Show ~P^~Q
Show ~P
P           ASS ID
P+Q         6 ADD
~(P+Q)      3 R
            7 8 ID
Show ~Q
Q           ASS ID
P+Q         11 ADD
~(P+Q)      3 R
            12 13 ID
~P^~Q       5 10 ADJ
            15 DD
            4 CD
Show ~P^~Q->~(P+Q)
~P^~Q       ASS CD
Show ~(P+Q)
P+Q         ASS ID
~P          19 SL
Q           21 22 MTP
~Q          19 SR
            23 24 ID
            20 CD
~(P+Q)<->~P^~Q     2 18 CB
            27 DD
```
- ex. Derive $S\lor R \to Q, \enskip {\sim}(P\lor {\sim}S) \enskip \therefore \enskip {\sim}(P\leftrightarrow Q)$ using DeMorgan's:
```xorg
Show ~(P<->Q)
P<->Q       ASS ID
S+R->Q      PR
~(P+~S)     PR
~P^~~S      4 DM
~P          5 SL
~~S         5 SR # could alternatively use ADD to build S+R
Q->P        2 BC
~Q          6 8 MT
~(S+R)      3 9 MT
~S^~R       10 DM
~S          11 SL
            7 12 ID
```
- ex. Derive $\therefore \enskip P \lor {\sim}P$ using a CDJ theorem:
```xorg
Show P+~P
Show ~P->~P # CDJ proof
~P          ASS CD
            3 DD
P+~P        2 CDJ
            9 DD

Show P+~P   # alternatively, using DM
~(P+~P)     ASS ID
~P^~~P      2 DM
~P          3 SL
~~P         3 SR
            4 5 ID
```
- ex. Derive $R \lor Q, \enskip Q \leftrightarrow (Q\to {\sim}R) \enskip\therefore\enskip {\sim}R \leftrightarrow Q$:
```xorg
Show ~R<->Q
R+Q         PR
Q<->(Q->~R) PR
Show ~R->Q
~R          ASS CD
Show Q
~Q          ASS ID
R           2 7 MTP
~R          5 R
            8 9 ID
            6 CD
Show Q->~R
Q           ASS CD
Show ~R
R           ASS ID
Q->(Q->~R)  3 BC
Q->~R       13 16 MP
~R          13 17 MP
            18 DD
            14 CD
~R<->Q      4 12 CB
            21 DD
```
- ex. Derive ${\sim}R\lor(P\leftrightarrow{\sim}S), \enskip {\sim}({\sim}R\to P)\to S \enskip \therefore\enskip P\lor S$:
```xorg
Show P+S
~(P+S)      ASS ID
~R+(P<->~S) PR
~(~R->P)->S PR
~P^~S       2 DM
~P          5 SL
~S          5 SR
~~(~R->P)   4 7 MT
~R->P       8 DN
~~R         6 9 MT
P<->~S      3 10 MTP
~S->P       11 BC
P           7 12 MP
            6 13 ID
```
- ex. Derive $\therefore \enskip (P\land R\to Q \lor S)\to (P\to Q)\lor(R\to S)$:
```xorg
Show (P^R->Q+S)->(P->Q)+(R->S)
P^R->Q+S    ASS CD
Show (P->Q)+(R->S)
~((P->Q)+(R->S))    ASS ID
~(P->Q)^~(R->S)     4 DM
~(P->Q)     5 SL
~(R->S)     5 SR
P^~Q        6 NC
R^~S        7 NC
P           8 SL
~Q          8 SR
R           9 SL
~S          9 SR
P^R         10 12 ADJ
Q+S         2 14 MP
S           11 15 MTP
            13 16 ID
            3 CD
```
- ex. Derive $(P\land Q)\to((R\lor S)\land{\sim}(R\land S)), \enskip S \to (R\land Q)\lor({\sim}R\land {\sim}Q)\lor{\sim}P, \enskip R\land Q \to S \enskip\therefore\enskip P\to{\sim}Q$:
```xorg
Show P->~Q
P           ASS CD
Show ~Q
Q           ASS ID
P^Q->(R+S)^~(R^S)   PR
S->(R^Q)+(~R^~Q)+~P PR
R^Q->S              PR
P^Q         2 4 ADJ
(R+S)^~(R^S)        5 8 MP
R+S         9 SL
~(R^S)      9 SR
~R+~S       11 DM
Show S
~S          ID
~(R^Q)      7 14 MT
~R+~Q       15 DM
~~Q         4 DN
~R          16 17 MTP
S           10 18 MTP
            14 19 ID
(R^Q)+(~R^~Q)+~P    6 13 MP
~~P         2 DN
(R^Q)+(~R^~Q)       21 22 MTP
Show ~(R^Q)
R^Q         ASS ID
R           25 SL
~~R         16 DN
~S          12 27 MTP
S           13 R
            28 29 ID
~R^~Q       23 24 MTP
~Q          31 SR
            4 32 ID
            3 CD
```
- ex. Proving one of the quantifier negation theorems.
```xorg
Show ~?xFx<->/x~Fx.
Show ~?xFx->/x~Fx.
~?xFx       ASS CD
Show /x~Fx.
Show ~Fx.
Fx          ASS ID
?xFx        6 EG
~?xFx       3 R
            7 8 ID
            5 UD
            4 D
Show /x~Fx->~?xFx.
/x~Fx       ASS CD
Show ~?xFx.
?xFx        ASS ID
Fi          15 EI
~Fi         13 UI
            16 17 ID
            14 CD
~?xFx<->/x~Fx   2 12 CB
            20 DD
```
## Quantifier Derivations
***

- ex. Derive $\exists x (Fx \land {\sim}Gx)\to\forall x(Fx\to Hx), \enskip \exists x(Fx\land Jx) \enskip\therefore\enskip \forall x(Fx \to {\sim}Hx)\to\exists x(Jx\land Gx)$ using quantifier theorems.
```xorg
Show /x(Fx->~Hx)->?x(Jx^Gx).
/x(Fx->~Hx) ASS CD
Show ?x(Jx^Gx).
~?x(Jx^Gx)  ASS ID
?x(Fx^~Gx)->/x(Fx->Hx)  PR
?x(Fx^Jx)   PR
/x~(Jx^Gx)  4 QN
Fi^Ji       6 EI
Fi          8 SL
Ji          8 SR
~(Ji^Gi)    7 UI
~Ji+~Gi     11 DM
~Gi         10 DN 12 MTP
Fi->~Hi     2 UI
~Hi         9 14 MP
Show ?x(Fx^~Gx).
~?x(Fx^~Gx) ASS ID
/x~(Fx^~Gx) 17 QN
~(Fi^~Gi)   18 UI
~Fi+~~Gi    18 DM
~~Gi        8 DN 20 MTP
~Gi         13 R
            21 22 ID
/x(Fx->Hx)  5 16 MP
Fi->Hi      24 UI
Hi          9 25 MP
            15 26 ID
            3 DC
```
- ex. Derive $\exists x(Fx\lor Ga), \enskip \forall x(Fx\to Gx) \enskip\therefore\enskip \exists xGx$.
```xorg
Show ?xGx.
~?xGx       ASS ID
/x~Gx       2 QN
?x(Fx+Ga)   PR
/x(Fx->Gx)  PR
Fi+Ga       4 EI
~Ga         3 UI
Fi          6 7 MTP
Fi->Gi      5 UI
Gi          8 9 MP
~Gi         3 UI
            10 11 ID
```
- ex. Derive $\therefore \enskip {\sim}\forall x \exists y (Fy\land {\sim}Fx)$.
```xorg
Show ~/x?y(Fy^~Fx).
/x?y(Fy^~Fx)    ASS ID
?y(Fy^~Fx)  2 UI
Fi^~Fx      3 EI
Fi          4 SL
~Fx         4 SR
?y(Fy^~Fi)  2 UI # have to re-UI
Fk^~Fi      7 EI
~Fi         8 SR
            5 9 ID
```
- ex. Derive $\forall x \exists y (Fx \lor {\sim}Gy), \enskip \exists x \forall y (Gy \lor Hx) \enskip\therefore\enskip {\sim}\exists xHx \to \forall xFx$.
```xorg
Show ~?xHx->/xFx.
~?xHx       ASS CD
Show /xFx.
Show Fx.
~Fx         ASS ID
/x?y(Fx+~Gy)    PR
?x/y(Gy+Hx)     PR
/x~Hx       2 QN
/y(Gy+Hi)   7 EI
?y(Fx+~Gy)  6 UI
Fx+~Gk      10 EI
~Gk         5 11 MTP
Gk+Hi       9 UI
Hi          12 13 MTP
~Hi         8 UI
            14 15 ID
            4 UD
            3 CD
```
- ex. Derive $\forall x (Jx\to\forall xIx), \enskip \forall x(Ix\to(Fx\to Gx\lor Hx)) \enskip\therefore\enskip \forall x(Jx\to \forall x(Fx\to(Gx\lor Hx)))$.
```xorg
Show /x(Jx->/x(Fx->Gx+Hx)).
Show Jx->/x(Fx->Gx+Hx).
Jx          ASS CD # x is free here
Show /x(Fx->Gx+Hx).
Show Fx->Gx+Hx.    # illegal, cannot do universal derivation here!

...
Show /x(Fx->Gx+Hx).
~/x(Fx->Gx+Hx)  ASS ID
?x~(Fx->Gx+Hx)  5 QN
/x(Jx->/xIx)    PR
/x(Ix->(Fx->Gx+Hx)) PR
~(Fi->Gi+Hi)    6 EI
Fi+~(Gi+Hi)     9 NC
~(Gi+Hi)    10 SR
~Gi^~Hi     11 DM
Fi          10 sl
~Gi         12 SL
~Hi         12 SR
Jx->/xIx    7 UI
/xIx        3 16 MP
Ii->(Fi->Gi+Hi) 8 UI
Ii          17 UI
Fi->Gi+Hi   18 19 MP
Gi+Hi       13 20 MP
Hi          14 21 MTP
            15 22 ID
            4 CD
            2 UD
```
- ex. Derive $\exists xFx \leftrightarrow \exists xGx \enskip\therefore\enskip \exists x\exists y(Fx\leftrightarrow Gy)$.
```xorg
Show ?x?y(Fx<->Gy).
~?x?y(Fx<->Gy)  ASS ID
?xFx<->?xGx     PR
/x~?y(Fx<->Gy)  2 QN # will QN later and become universal
Show ?xFx.
~?xFx       ASS ID
~?xGx       3 6 BT
/x~Fx       6 QN
~Fx         8 UI
/x~Gx       7 QN
~Gx         10 UI
~?y(Fx<->Gy)    4 UI
/y~(Fx<->Gy)    12 QN
~(Fx<->Gx)      13 UI
Fx<->~Gx    14 NB
~~Gx        9 15 BT
            11 16 ID
?xGx        3 5 BP
Fi          5 EI
Gk          18 EI
~?y(Fi<->Gy)    4 UI
/y~(Fi<->Gy)    21 QN
~(Fi<->Gk)      22 UI
Fi<->~Gk    23 NB
~Gk         19 24 BP
            20 25 ID
```
- ex. Derive $\exists x(Fx\leftrightarrow P), \enskip \exists x(Gx \leftrightarrow P), \enskip \forall x(Fx \leftrightarrow {\sim}Gx) \enskip\therefore\enskip \exists x\exists y (Fx\land {\sim}Gx\leftrightarrow Gy\land{\sim}Fy)$.
```xorg
Show ?x?y(Fx^~Gx<->Gy^~Fy).
~?x?y(Fx^~Gx<->Gy^~Fy)  ASS ID
?x(Fx<->P)      PR
?x(Gx<->P)      PR
/x(Fx<->~Gx)    PR
Fi<->P      3 EI
Gk<->P      4 EI
Fi<->~Gi    5 UI
Fk<->~Gk    5 UI
/x~?y(Fx^~Gx<->Gy^~Fy)  2 QN
~?y(Fi^~Gi<->Gy^~Fy)    10 UI
/y~(Fi^~Gi<->Gy^~Fy)    11 QN
~(Fi&~Gi<->Gk^~Fk)      12 UI
Fi^~Gi<->~(Gk^~Fk)      13 NB
Show P.
~P          ASS ID
~Fi         6 16 BT
~Gk         7 16 BT
~~Gi        8 17 BT
Fk          9 18 BP
Show ~(Gk^~Fk).
Gk^~Fk      ASS ID
Gk          22 SL
~Gk         18 R
            23 24 ID
Fi^~Gi      14 21 BP
Fi          26 SL
            17 27 ID
Fi          6 15 BP
Gk          7 15 BP
~Gi         8 29 BP
~Fk         30 DN 9 BT
Fi^~Gi      29 31 ADJ
~(Gk^~Fk)   14 33 BP
~Gk+~~Fk    34 DM
~~Fk        30 DN 35 MTP
            32 36 ID
```
- ex. Derive ${\sim}Fx \lor \forall xFx \enskip\therefore\enskip {\sim}Fx\to{\sim}\exists xFx$.
```xorg
Show /x(~Fx+/xFx). # performing a universal closure on the free x
~Fx+/xFx    PR
            2 UD
Show ~Fx->~?xFx.
~Fx         ASS CD
Show ~?xFx.
?xFx        ASS ID
Fi          7 EI
~Fi+/xFx    1 UI   # allows us to reinstantiate the x to i
/xFx        8 DN 9 MTP
Fx          10 UI
~Fx         5 R
            11 12 ID
            6 CD
```
- ex. Derive $\therefore \enskip \forall xFx \leftrightarrow \forall yFy$.
```xorg
Show /xFx<->/yFy.
Show /xFx->/yFy.
/xFx        ASS CD
Show /yFy.
Fy          3 UI
            5 UD
            4 CD
Show /yFy->/xFx.
/yFy        ASS CD
Show /xFx.
Fx          9 UI
            11 UD
            10 CD
```
# Validity and Invalidity
***

- a **valid** argument is one where it is impossible for the premises all to be true and the conclusion false:
    - to show an argument is **invalid**, we need to construct a **counterexample**
    - for sentential logic, we used truth tables to prove argument were invalid
        - truth tables grew quite large with many sentence letters
    - can we use a shortcut?

- ex. Prove the argument $P\land Q \to R \enskip \therefore \enskip P\lor Q \to R$ is invalid:
    - focus into a *single* row of the table instead of the entire table
    - need to show premise is true and conclusion is false
    - to make the conclusion false, need to make the conditional false:
        - need to make $P \lor Q$ true and $R$ false
        - $R$ is false in the premise as well
    - make $P$ true in the disjunction
        - to make premise false, need a true conditional
    - $R$ is false, so we can make $Q$ either true or false to make the premise false
    - thus the counterargument is where $R$ is false and $P, Q$ are true

- ex. Prove the argument ${\sim}S \to P, \enskip Q\lor R \to {\sim}S, \enskip Q\to W, \enskip R\to W, \enskip {\sim}(P\land V) \enskip \therefore \enskip {\sim}S \to W$ is invalid:
    - show premises are true and conclusion false:
        - only way to show conditional is false is with a true antecedent and a false consequent
        - thus $S, W$ are both false
    - now, need to show every premise to be true:
        - for the first premise, $P$ must be true
        - the next premise will always be true
        - for the next premises, $Q, R$ must be false
        - for the last premise, $V$ must be false
    - thus the counterargument is where $P$ is true and all other variables are false

- ex. The argument $\exists xFx, \enskip \forall x(Fx\to Gx). \enskip \exists x{\sim}Gx \enskip \therefore \enskip \forall x(Gx\to Fx)$.
    - argument seems invalid, can we construct a counterexample?
    - show premise is true and conclusion false
        - how do we make quantifiers true or false?
            - need to create a *"universe"* where the quantifiers are true or false
    - make an object 0:
        - has property $F$
        - satisfies first premise
        - to satisfy second premise, this object also has property $G$
    - make an object 1:
        - to make conclusion false, we need something that has property $G$ but not $F$
        - give object property $G$ and property ${\sim}F$
    - make an object 2:
        - to satisfy third premise, give object property ${\sim}G$
        - also give object property ${\sim}F$ to ensure that the second property is not violated

- ex. Prove the argument $\exists X(Fx\land {\sim Gx}, \enskip \forall x(Hx\to {\sim}Gx), \enskip \exists x(Hx\land Fx)) \enskip\therefore\enskip \forall x(Fx \to {\sim}Gx)$ is invalid.
    - make an object 0:
        - has property $F$ and $G$ to make conclusion false
    - make an object 1:
        - has property $F$ and ${\sim}G$ to make first premise true
        - also has property $H$ to make third premise true
        - also satisfies second premise
    - in general, existential quantifiers in premises and universal quantifiers in the conclusion are easy to handle

- ex. Prove the argument $\forall x(Fx\to (Gx\leftrightarrow Hx)), \enskip Ga \land {\sim}Ha \enskip \therefore \enskip \forall x{\sim}Fx$ is invalid.
    - make an object 0:
        - has property $F$ to make conclusion false
    - make an object 1:
        - has property $G, H$ to satisfy second premise
        - also name this object $a$
    - note that the first premise is satisfied by both objects

- ex. Prove the argument $\exists xFx \land \forall xGx \to P \enskip\therefore\enskip \forall xFx\land \exists xGx \to P$ is invalid.
    - a sentence letter can be true or false
        - to make conclusion false, set $P$ false
    - make an object 0:
        - has property $F$ and $G$ to make antecedent of the conclusion true
    - make an object 1:
        - to make premise true, antecedent has to be false
        - thus $\forall xGx$ must be false, so object has property ${\sim}G$
        - to *keep* antecedent of conclusion true, need to also have property $F$

- useful confinement and distribution theorems for quantifiers:
    - $\therefore \enskip \forall x(P\land Fx) \leftrightarrow P \land \forall xFx$ AKA universal confinement over a conjunction:
        - similarly for $\forall X(Fx \land P)$ and for disjunctions
        - similarly for existential quantifiers
    - for conditionals, we have $\therefore\enskip \forall x(P\to Fx) \leftrightarrow (P\to \forall xFx)$:
        - similarly for existential quantifiers
        - however, for confinement with the antecedent, we have $\therefore\enskip \forall x(Fx\to P) \leftrightarrow (\exists xFx \to P)$
            - similarly for existential quantifiers
    - $\therefore \exists x(Fx\lor Gx)\leftrightarrow \exists xFx  \lor \exists xGx$ AKA existential distribution
    - $\therefore \forall x(Fx\land Gx)\leftrightarrow \forall xFx  \land \forall xGx$ AKA universal distribution

- ex. Prove the argument $\forall x(Fx\to \forall yGy), \enskip \exists xFx \enskip \therefore\enskip \forall yFy$ is invalid.
    - can rewrite first premise as $\exists xFx \to \forall yGy$
    - make an object 0:
        - has property ${\sim}F$ to make conclusion false
        - has property $G$ to satisfy first premise
    - make an object 1:
        - has property $F$ to satisfy second premise
        - has property $G$ to satisfy first premise
    - can alternatively do a truth-functional expansion given a fixed number of objects:
        - argument is equivalent to $((F0 \to G0 \land G1) \land (F1 \to G0\land G1)), \enskip F0 \lor F1 \enskip\therefore\enskip F0\land F1$ in a universe of two objects
        - can work backwards in the truth table on this equivalent argument without qualifiers to prove invalidity as well
        - also gives object 0 with property $G$ and ${\sim}F$ and object 1 with property $F, G$

- ex. Prove the argument $\forall x \exists y(Fx\leftrightarrow {\sim}Fy), \enskip \exists x(Fx\land Gx) \enskip\therefore\enskip \forall xFx$ is invalid.
    - no theorem handles the $\forall x \exists y$, so try performing a truth-functional expansion with two objects:
        - $((F0\leftrightarrow{\sim}F0)\lor(F0\leftrightarrow{\sim}F1))\land((F1\leftrightarrow{\sim}F0)\lor(F1\leftrightarrow {\sim}F1))$
        - $(F0\land G0)\lor(F1\land G1)$
        - $\therefore\enskip F0\land F1$
    - to make conclusion false, make one conjunct false
        - make $F0$ false
    - for second premise, need to make $F1, G1$ true
    - with these settings, the first premise is true
        - if it ended up false, would have had to make the universe larger
    - counterexample is thus:
        - object 0 with either no properties or $G$
        - object 1 with property $F, G$
    - alternatively, instead of performing an expansion, we can attempt to perform a derivation:
        - derivation will never complete since the argument is invalid
            - since derivation cannot be concluded after the initial assumption, there must be a way for all premises to be true and the conclusion false
        - take all the atomic sentences
            - here, EIs and UIs in the derivation give
                - ${\sim}Fx, Fi, Gi, {\sim}Fm, Fk, {\sim}Fo, Fp$
        - whenever we instantiate in a derivation, essentially creating an object that can be used in a counterexample
            - in this case, we have 6 objects

- ex. Prove the argument $\forall x \exists y (Fx\lor Gy \to Hy), \enskip \forall xGx \lor \exists xGx \enskip\therefore\enskip \forall x(Fx\lor Hx)$ is invalid.
    - use the failed derivation approach:
        - gives ${\sim}Fx, {\sim}Hx, Gx, Gi, Hi$
        - let $x$ be object 0 and $i$ be object 1
        - gives us desired counterexample

Using the failed derivation:
```xorg
Show /x(Fx+Hx).
Show Fx+Hx.
~Fx^~Hx         ASS ID DM
~Fx             3 SL
~Hx             3 SR
?x/x(Fx+Gy->Hy) PR
/xGx+?xGx       PR
/x(Fx+Gi->Hi)   6 EI
Show ~/xGx.
/xGx            ASS ID
Fx+Gi->Hi       8 UI
Fi+Gi->Hi       8 UI
Gx              10 UI
Gi              10 UI
Fx+Gi           14 ADDL
Hi              11 15 MP
```
