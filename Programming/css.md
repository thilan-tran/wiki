---
title: "CSS"
mainfont: Libertinus Serif
monofont: Iosevka
fontsize: 14pt
geometry: margin=2cm
toc: true
documentclass: extarticle
header-includes: |
  \hypersetup{colorlinks=true,linkcolor=black,urlcolor=myblue}
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \usepackage{fvextra}
  \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
  \usepackage{xcolor}
  \definecolor{mygray}{HTML}{A6A5A2}
  \definecolor{mygreen}{HTML}{98C379}
  \definecolor{myblue}{HTML}{61AFEF}
  \definecolor{mycyan}{HTML}{56B6C2}
  \definecolor{myorange}{HTML}{E5C07B}
  \definecolor{myred}{HTML}{E06C75}
  \definecolor{mypurple}{HTML}{AE81FF}
  \usepackage{caption}
  \usepackage{listings}
  \lstset{
  basicstyle=\ttfamily,
  captionpos=t,
  title=\lstname,
  columns=fullflexible,
  lineskip=2pt,
  breakatwhitespace=false,
  breaklines=true,
  extendedchars=true,
  keepspaces=true,
  showspaces=false,
  showtabs=false,
  tabsize=2,
  frame=trbL,
  numbersep=9pt,
  stepnumber=2,
  backgroundcolor=\color{gray!10}}
  \usepackage{microtype}
---

# CSS
***

## Floating
***

- can **float** elements out of normal document flow
  - `float: left;` and `float: right;`
  - generates elements organized vertically
  - eg. text columns
- often use **clear** property after a float
  - `someClass:after { clear: both; }`

## Flexbox
***

- a CSS display type
  - positions elements relative to their parents and each other
  - works *responsively* as well

- flex container:
  - `display: flex;`
  - `flex-wrap: wrap;`
    - wraps elements along the cross axis as browser shrinks
    - `wrap-reverse` wraps elements above
    - `nowrap` default
  - `justify-content: center;`
    - centers elements in container along the main axis
    - `flex-end`, `flex-start` (default)
    - `space-around`, `space-between`
  - `align-items: center;`
    - centers elements in container along the cross axis
    - `flex-end`, `flex-start` (default)
  - `flex-flow: column`
    - main axis now vertical, now the cross axis is horizontal
    - `column-reverse`, `row-reverse`, `row` (default)

- items within flex container:
  - `flex-grow: 1;`
    - specifies growth rate compared to siblings when expanding in the container
  - `flex-shrink: 1;`
    - specifies shrink rate compared to siblings as browser shrinks (default is equal)
  - `flex-basis: 200px;`
    - essentially an initial width for elements (along the cross axis)
    - unlike `minimum-width`, elements can shrink below this width
  - can combine the above properties:
    - `flex: 1 0 200px;` (grow, shrink, basis)
    - `flex: 1;` (grow and shrink 1, basis defaults to 0)
  - `order` changes the order of elements
    - lower order comes first, defaults to 0

Simple Navbar Example:
```
/* default to dropdown-style navbar */
nav ul {
  list-style-type: none;
  padding: 0;
}

nav a {
  text-decoration: none;
  text-align: center;
  color: #fff;
  display: block;
  padding: 10px;
}

nav a:hover {
  background-color: #555;
}

@media screen and (min-width: 768px) {
  /* flexbox above certain width */
  nav ul {
    display: flex;
  }

  nav li {
    flex: 1 1 0;
  }
}
```
