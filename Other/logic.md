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
  2. John got thirsty $\therefore$ John ate pizza.
  - *invalid* argument

- ex. argument:
  1. If John eats pizza he will get thirsty.
  2. If John does not eat pizza he will be hungry.
  3. If John will not get sick he will not be hungry.
  4. $\therefore$ John will get sick.
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
  - sentence letters are $P, Q, R, \dots, Z$
    - with or without subscripts
  - sentential connectives:
    - $\land$ ie. "and", $\lor$ ie. "or", $\to$ ie. "if-then", $\leftrightarrow$ ie. "if and only if"
    - ${\sim}$ ie. "it is not the case that"
  - punctuation is parantheses

- ex. Peter loves pizza.
  - this is an **atomic** sentence that cannot be broken up further
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
  3. if a binary connective is placed between two symbolic sentences and enclosed in parentheses,the result is a symbolic sentence
  - eg. $P, Q, (P \to Q), {\sim} P, ({\sim} P\leftrightarrow(P\to Q))$ are all symbolic sentences
  - informal conventions:
    1. outermost parentheses may be omitted
    2. conditionals and biconditionals are assumed to *outrank* conjunctions and disjunctions:
        - thus parentheses may be omitted around conjunctions and disjunctions when there is no ambiguity
        - eg. a reduction like $P \lor Q \land R$ is ambiguious
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
  - $~P \land ~Q = ~(P \lor Q)$

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
