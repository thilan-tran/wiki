---
title: "Full Stack"
date: "Summer 2019"
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
  language=c++,
  basicstyle=\ttfamily,
  commentstyle=\color{mygray}\textit,
  keywordstyle=\color{mycyan}\bfseries,
  identifierstyle=\color{mygreen},
  stringstyle=\color{myorange},
  directivestyle=\color{mypurple},
  numberstyle=\small\color{mygray},
  rulecolor=\color{mygray},
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
  literate=%
    {0}{{{\color{mypurple}0}}}1
    {1}{{{\color{mypurple}1}}}1
    {2}{{{\color{mypurple}2}}}1
    {3}{{{\color{mypurple}3}}}1
    {4}{{{\color{mypurple}4}}}1
    {5}{{{\color{mypurple}5}}}1
    {6}{{{\color{mypurple}6}}}1
    {7}{{{\color{mypurple}7}}}1
    {8}{{{\color{mypurple}8}}}1
    {9}{{{\color{mypurple}9}}}1
    {+}{{{\color{myred}+}}}1
    {-}{{{\color{myred}-}}}1
    {>}{{{\color{myred}>}}}1
    {<}{{{\color{myred}<}}}1
    {=}{{{\color{myred}=}}}1
    {\ *\ }{{{\color{myred}\ *\ }}}1
    {\ /\ }{{{\color{myred}\ /\ }}}1,
  backgroundcolor=\color{gray!10}}
  \usepackage{microtype}
---


# Full Stack Course
***

## Basics
***

- server and web browser communicate through **HTTP** protocol
  - browser makes *requests*, server *responds* to requests
    - every webpage makes requests to GET requests to static files on load:
      - eg. HTML page, CSS style sheet, JS script file
  - request types include GET, POST, etc.
  - response headers define status code, response size, time, content-type
- traditionally, application logic is on the *server*
- however, *browser* can:
  - application logic using requests for data (with AJAX) to fetch dynamic content
  - modify the HTML being rendered through the **Document Object Model** (DOM)
- a **Single Page Application** (SPA) comprises of only one HTML page
  - contents are manipulated with JS in the browser
  - rather than having separate pages fetched from the server

AJAX and dynamic content with pure Javascript:
```js
var xhttp = new XMLHttpRequest();

/* attaching a callback to an event handler */
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const data = JSON.parse(this.responseText);
    console.log(data);
  }

  /* DOM manipulation */
  var ul = document.createElement('ul');
  ul.setAttribute('class', 'notes');

  data.forEach(function(note) {
    var li = document.createElement('li');
    ul.appendChild(li);
    li.appendChild(document.createTextNode(note.content));
  })

  document.getElementById('notes').appendChild(ul);
}

xhttp.open('GET', '/data.json', true);
xhttp.send();

/* AJAX POST */
xhttpPost = new XMLHttpRequest();
xhttpPost.open('POST', '/new_note', true);
xhttpPost.setRequestHeader('Content-type', 'application/json');
xhttpPost.send(JSON.stringify(note));
```

## Front-End Testing and Custom Hooks
***

### Custom Hooks
***

- **custom hooks** extract component logic into resuable functions
  - follow general *hook rules*:
    - don't call hooks inside loops, conditionals, or nested functions
    - only call from React function components or other custom hooks
  - names start with `use` by convention

Counter custom hook:
```js
const useCounter = () => {
  const [val, setVal] = useState(0);

  const increase = () => setVal(val+1);
  const decrase = () => setVal(val-1);
  const zero = () => setVal(0);

  return { val, increase, decrease, zero };
}

const App = () => {
  /* two separate counters */
  const left = useCounter();
  const right = useCounter();

  ...
  <button onClick={right.increase}>add to right</button>
  ...
}
```
Form-field custom hook:
```js
const useField = (type) => {
  const [value, setValue] useState('');

  const onChange = (e) => setValue(e.target.value);

  /* matching methods to property names
     allows spread syntax to be used */
  return { type, value, onChange };
}

const App = () => {
  const name = useField('text');
  const born = useField('date');

  return (
    <form>
      name:
      <input {...name} />
      birthdate:
      <input {...born} />
    </form>
  )
}
```
## Redux
***

- **Flux** is a *state-management* alternative
  - previously, state was stored in the root component
  - passed down other components through props
- state is separated from components into a **store**
- the store is changed with **actions**
  - objects with at least a type field
  - actions are *dispatched* to the store
  - can abstract actions with functions, called **action creators**
- the impact of the action on the store is defined with a **reducer**
  - function taking current state and action as parameters
  - returns a new state (with immutable objects)
    - test immutability with `deep-freeze` module
- get current state with `store.getState()`
- call callback functions on store change with `store.subscribe(callbackFunc)`
  - react will *not* automatically re-render on store change

- *note*: **uncontrolled** forms do not have the state of the form fields bound to the component state
  - limitations include no dynamic errors or disabling submit button

Counter with Redux:
```js
import { createStore } from 'redux';

const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state+1;
    case 'DECREMENT':
      return state-1;
    case 'ZERO':
      return 0;
    default:
      return state;
  }
}

/* reducer is never called directly */
const store = createStore(counterReducer);

store.dispatch({type: 'INCREMENT'});

console.log(store.getState())
```
Notes app with Redux:
```js
const noteReducer = (state = [], actions) => {
  switch(action.type) {
    case 'NEW_NOTE':
      /* use immutable array methods (ie. concat, spread syntax) */
      return [...state, action.data];
    case 'TOGGLE_IMPORTANCE':
      const id = action.data.id;
      const noteToChange = state.find(n => n.id === id);
      const changedNote = {
        ...noteToChange,
        important: !noteToChange.important
      };

      return state.map(note => note.id !== id ? note : changedNote);
    default:
      return state;
  }
}

const createNote = (content) =>
  { type: 'NEW_NOTE', data: { content, important: false, id: generateId() }};

const createNote = (id) =>
  { type: 'TOGGLE_IMPORTANCE', data: { id }};

store.dispatch(createNote(content));

const render = () => {
  ReactDOM.render(...);
};

/* first initiol render, required */
render();
/* re-render on store update */
store.subscribe(render);
```
### Complex Redux Stores
***

- options for sharing the store among components:
  - pass the store as a prop
  - use `connect()` from React-Redux library
    - components must be a child of `Provider` component
      - ie. a *connected component*
      - `mapStateToProps()` and `mapDispatchToProps()` allow store to be manipulated through props

Using `Provider` HOC:
```js
import { Provider } from 'react-redux';
...
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```
Using `connect()`:
```js
import { connect } from 'react-redux';

const Notes = ...

const mapStateToProps = (state) => {
  return {
    /* accessing reducers' state from props directly */
    notes: state.notes,
    filter: state.filter
  };
};

/* simplifying mapping the state with a selector function */
const notesToShow = ({ notes, filter }) => {
  if (filter === 'ALL') return notes;

  return filter === 'IMPORTANT' ? notes.filter(note => note.important)
                                : notes.filter(note => !note.important);
}

const mapStateToProps = (state) => {
  return {
    visibleNotes: notesToShow(state)
  }
}

/* automatically dispatches action from action creator */
const mapDispatchToProps = {
  /* dispatching action from action creator from props directly */
  toggleImportanceOf
};

/* alternative, explicit function syntax for mapping dispatch */
const mapDispatchToProps = (dispatch) => {
  return {
    toggleImportanceOf: (id) => dispatch(toggleImportanceOf(id))
  };
};

const ConnectedNotes = connect(mapStateToProps, mapDispatchToProps)(Notes);
export default ConnectedNotes;
```
- combine multiple stores / reducers together:
  - `combineReducers(combinedObj)`

- *note*: *presentational* components are simple, their event handlers are abstracted
  - visual, DOM markup and styles, no dependencies, receive data and callbaks exclusively through props
- while *container* components contain application logic, such as defining event handlers
  - no DOM markup, data handling, stateful, HOC's

Combining multiple reducers:
```js
import { createStore, combineReducers } from 'redux';
import noteReducer from './reducers/noteReducer';
import filterReducer from './reducers/filterReducer';

const reducer = combineReducers({
  notes: noteReducer,
  filter: filterReducer
});

const store = createStore(reducer);

/* access a reducer through store.getState().notes */
```
### Asynchronous Actions
***

- *redux-thunk* library allows for action creators to be asynchronous functions
  - eg. communicate / update data from a database
  - previously not possible to implement within an action creator
```js
import { applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

...

const store = createStore(reducer, applyMiddleware(thunk));

/* action creators can now have asynchronous operations */

export const initializeNotes = () => {
  return async (dispatch) => {
    const notes = await noteService.getAll();
    dispatch({ type: 'INIT_NOTES', data: notes });
  }
}

export const createNote = (content) => {
  return async (dispatch) => {
    const newNote = await noteService.createNew(content);
    dispatch({ type: 'NEW_NOTE', data: newNote })
  }
}
```
## React Router and Styling
***

### React Router
***

- *routing* is the navigation management of an application
  - React router from `react-router-dom` is a routing solution
- `Link` component modifies the url in address bar
- url-based component rendering defined with `Route` component
  - match exact paths to only catch parent components
  - access `match` parameter for url variables

Using the React BrowserRouter:
```js
import {
  BrowserRouter as Router,
  Route, Link, Redirect, withRouter
} from 'react-router-dom';

const App = () => {
  return (
    <Router>
      <div>
        /* navbar elements */
        <Link to="/">home</Link>
        <Link to="/notes">notes</Link>
        <Link to="/users">users</Link>
      </div>

      /* rendering components based on url */
      <Route exact path="/" render={() => <Home />} />
      <Route exact path="/notes" render={() => <Notes />} />
      <Route path="/notes/:id" render={({ match }) =>
        <Note note={noteById(match.params.id)} />
      } />
      <Route path="/users" render={() => <Users />} />

      /* conditional rendering */
      {user
       ? <em>{user} logged in</em>
       : <Link to="/login">login</Link>
      }
    </Router>
  )
}

const Notes = (props) => (
  ...
    <Link to={'/notes/' + note.id}>{note.content}</Link>
  ...
)
```
Using `withRouter` and `history` to change pages:
```js
import {
  withRouter
} from 'react-router-dom';

const Login = (props) => {
  const onSubmit = (e) => {
    e.preventDefault();
    ...
    /* render home after login */
    props.history.push('/');
  }

  return ...
}

/* add history prop to component */
const LoginWithHistory = withRouter(Login);
```
Using `redirect` to redirect routes:
```js
<Route path="/users" render={() =>
  user ? <Users /> : <Redirect to="/login" />
} />
```
### Styles
***

- **UI Frameworks** are predefined style themes and components
  - eg. Boostrap, Semantic UI, reactstrap, react-bootstrap
  - install CSS stylesheet and npm package

- Bootstrap basics:
  - entire application rendered in a `container` class
  - provides response designs
  - react-bootstrap offers:
    - `Table` component
      - striped, bordered, hover options
    - `Form` component
      - Group, Control, Label subcomponents
    - `Button` component
      - primary, secondary, success variants
    - `Alert` component (same variants) for notifications
    - `Navbar` component
      - Toggle, Collapse, Link subcomponents

- Semantic UI basics:
  - `Container` component
  - `Table` component
    - striped, celled options
    - Body, Row, Cell subcomponents
  - `Form` component
    - Field subcomponent
  - `Message` component
  - `Menu` component
    - Item subcomponent

- **Styled Components** use template literals for defining styles

Using React styled components:
```js
import styled from 'styled-components';

const Navigation = styled.div`
  background: grey;
  padding: 1em;
`

const Input = styled.input`
  margin: 0.25em;
`

<Input type='password' />
```
### Webpack
***

- **Webpack** bundles separate modules into one for the browser
  - `npm run build` bundles source code into build directory
  - also handles *transpiling* to bridge JS versions

Webpack configuration from scratch:

1. set up the following directory tree:
  - `build`
  - `package.json` (empty dependencies)
  - `src`
    - `index.js`
  - `webpack.config.js`
2. install webpack:
  - `npm install --save-dev webpack webpack-cli`
3. define `webpack.config.js`
4. define new npm script
  - `"build": "webpack --mode=developement"`

webpack.config.js:
```js
const path = require('path');

const config = {
  /* entry point for bundling */
  entry: './src/index.js',
  output: {
    /* __dirname holds current directory */
    path: path.resolve(__dirname, 'build'),
    /* bundled code */
    filename: 'main.js'
  }
};
module.exports = config;
```
Webpack with minimal React:

1. install react: `npm install --save react react-dom`
2. need minimal `build/index.html` file for react to render on
  - link to bundled `./main.js` in script tag
3. install babel and other dependencies:
  - `npm install --save-dev @babel/core babel-loader @babel/preset-react`
  - need polyfill for promises/async/await in some browsers:
    - `npm install --save-dev @babel/polyfill`
    - using library directly:
      - `import PromisePolyfill from 'promise-polyfill'`
      - `if (!window.Promise) window.Promise = PromisePolyfill;`
  - for transpiling preset:
    - `npm install --save-dev @babel/preset-env`
  - for css loaders: (injected directly into bundled code)
    - `npm install --save-dev style-loader css-loader`
4. configure config with babel to process JSX

webpack.config.js:
```js
const config = {
  entry: './src/index.js',
  /* for polyfill dependency */
  entry: ['@babel/polyfill', './src/index.js'],
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'main.js'
  },
  module: {
    rules: [
      {
        /* specifying .js files */
        test: /\.js$/,
        /* specifying loader */
        loader: 'babel-loader',
        /* specifying loader parameters */
        query: {
          presets: ['@babel/preset-react'],
          /* transpiling preset */
          presets: ['@babel/preset-env', '@babel/preset-react'],
        }
      },
      /* css loaders */
      {
        test: /\.css$/,
        loader: `babel-loader`,
        query: {
          presets: ['style-loader', 'css-loader'],
        }
      }
    ]
  }
};
```
Improved webpack developement workflow:

1. install webpack server:
  - `npm install --save-dev webpack-dev-server`
2. define npm script for server:
  - `"start": "webpack-dev-server --mode=developement"`
3. add config for server

webpack.config.js:
```js
const config = {
  output: ...,
  devServer: {
    contentBase: path.resolve(__dirname, 'build'),
    compress: true,
    port: 3000
  },
  /* map errors to original source code */
  devTool: 'source-map',
  ...
}
```
Minifying the code:

1. UglifyJS plugin automatically configured with webpack:
  - significantly reduces bundled code size
  - modify npm script mode:
    - `"build": "webpack --mode=production"`

Configuring backend integration (eg. server url):
```js
const webpack = require('webpack');

const config =  (env, argv) => {
  const BACKEND_URL = argv.mode === 'production'
    ? '...'
    : 'localhost...';

  return {
    entry: ...,
    output: ...,
    devServer: ...,
    ...
    plugins: [
      /* defining global default constraints in bundled code */
      new webpack.DefinePlugin({
        /* BACKEND_URL can be used directly in code */
        BACKEND_URL: JSON.stringify(BACKEND_URL)
      })
    ]
  }
}
```
### Class Components
***

- React *class* components:
  - use a constructor
    - initializes state (single object composed of multiple parts)
    - state can be set with `setState`
  - implement a render function
  - have access to React **lifecycle** methods
    - eg. `componentDidMount` is executed after first render

Class component example:
```js
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      anecdotes: [],
      current: 0
    };
  };

  componentDidMount = () => {
    axios.get(url).then(res => this.setState({ anecdotes: res.data }));
  }

  handleClick = () => {
    const current = Math.round(Math.random() * this.state.anecdotes.length);
    this.setState({ current });
  }

  render() {
    if (!this.state.anecdotes.length)
      return <div>no anecdotes...</div>;
    return (
      <div>
        <h1>anecdote of the day</h1>
        <div>{this.state.anecdotes[this.state.current].content}</div>
        <button onClick={this.handleClick}>next</button>
      </div>
    )
  }
}
```
vs. example as a functional component:
```js
const App = () => {
  const [aneccdotes, setAnecdotes] = useState([]);
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    axios.get(url).then(res => setAnecdotes(res.data));
  }, [])

  const handleClick = () => {
    setCurent(Math.round(Math.random() * aneccdotes.length));
  }

  if (!anecdotes.length)
    return <div>no anecdotes...</div>;

  return (
    <div>
      <h1>anecdote of the day</h1>
      <div>{anecdotes[current].content}</div>
      <button onClick={handleClick}>next</button>
    </div>
  )
}
```
### End to End Testing
***

- *End-to-End* (E2E) tests inspect the entire system
  - eg. Selenium, puppeter, Cypress
- Cypress start script: `cypress open`

- for controlling the state of database during tests:
  - create router specifically for tests
  - only register the router if app is run in test mode

Cypress test examples:
```js
describe('Note app', () => {
  beforeEach(() => {
    const user = {...};
    /* add user to db before every test */
    cy.request('POST', url, user);
    cy.visit(url);
  });

  it('front page can be opened', () => {
    cy.contains('Notes');
  });

  it('login form can be opened', () => {
    cy.contains('log in').click();
  });

  it('user can login', () => {
    cy.contains('log in').click();
    /* css selectors */
    cy.get('#username').type('user');
    cy.get('#password').type('pass');
    cy.contains('login').click();
    cy.contains('user logged in');
  });
})
```
### Miscellaneous
***

- [Structure Organization in a React App](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed)
- frontend can be deployed separately from backend

- options for watching for changes on server from frontend:
  - *poll* on the frontend (repeated requests to API using `setInterval`)
  - **WebSockets** establish a two-way communication bewteen browser and server
    - define callback functions when server updates state
    - Socket.io library provides fallback options if unsupported

- React uses *virtual DOM*:
  - real DOM is never directly manipulated
  - fast, only updates necessary elements on DOM change

- React deals with the *views* in Model-View-Controller (MVC) architecture
  - Flux architecture makes React even more focused on views

- application security:
  - **injection** is text sent through a form
  - **SQL-injection** maliciously modify the database with SQL queries
    - prevented by *sanitizing* the input
  - mongoose automatically santizes its queries
  - **Cross-site scripting** (XSS) injects malicious JS code into app

- current trends:
  - typed JS versions, eg. Typescript
  - *server-side* rendering allows for **Search Engine Optimization** (SEO)
  - *isomorphic* applications are rendered on both front and backend
  - *universal* applications can be executed on both front and backend
  - **Progressive Web Apps** (PWA) work on every platform
    - should work well with limited or no connections
    - offline functionality implemented with *service workers*
  - *monolithic* backend runs on a single server with a few API-endpoints
  - *microservice* architecture composes backend from separate, independent services
  - *serverless* applications use Cloud functions, easily scalable

- other libraries:
  - Immer, immutable.js for immutable data structures
  - Redux-saga alternative for thunk
  - React Google Analytics for SPA analytics
  - React Native for mobile developement
  - Parcel alternative for webpack

## GraphQL
***

- **GraphQL** is an alternative to REST API
  - REST is *resource based*, every resource has an address
  - with GraphQL, browser makes a JSON-like query with a POST request
    - all queries are sent to the same address
    - schemas describe data sent between client and server

### Schemas
***
```js
type Person {
  /* ! indicates required field */
  name: String!
  phone: String
  street: String!
  city: String!
  /* unique ID type (string) */
  id: ID!
}

/* describes what queries can be made */
type Query {
  /* ! indicated non-null return/parameter types */

  /* always returns an integer */
  personCount: Int!

  /* always returns list of Persons, without any null values */
  allPersons: [Person!]!

  /* requires string paramter, returns person or null */
  findPerson(name: String!): Person
}
```
### Queries and Responses
***
```js
query {
  personCount
}

{
  "data": {
    "personCount": 3
  }
}

query {
  allPersons {
    /* must describe which fields of Person to return */
    name
    phone
  }
}

{
  "data": {
    "allPersons": [
      {
        "name": ...,
        "phone": ...
      },
      ...
    ]
  }
}

query {
  findPerson(name: "R2D2") {
    phone
    city
    street
    id
  }
}

{
  "data": {
    "findPerson": {
      "phone": ...,
      "city": ...,
      "street": ...,
      "id": ...
    }
  }
}

/* null response */
{
  "data": {
    "findPerson": null
  }
}

/* combining queries */
query {
  personCount
  allPersons {
    name
  }
}

{
  "data": {
    "personCount": 3,
    "allPersons": [
      { "name": ... },
      { "name": ... },
      { "name": ... }
    ]
  }
}

/* renaming queries */
query {
  havePhone: allPersons(phone: YES) {
    name
  }
  phoneless: allPersons(phone: NO) {
    name
  }
}

{
  "data": {
    "havePhone": [
      { "name": ... },
      { "name": ... }
    ],
    "phoneless": [
      { "name": ... }
    ]
  }
}
```
### Resolvers
***
```js
const { ApolloServer, gql } = require('apollo-server');

let persons = [
  {
    name: ...,
    phone: ...,
    street: ...,
    city: ...,
    id: ...
  },
  ...
];

/* GraphQL schema */
const typeDefs = gql`
  /* schema doesn't necessarily match stored object */
  type Address {
    street: String!
    city: String!
    /* no id field since address not saved on server */
  }

  type Person {
    name: String!
    phone: String
    address: Address!
    id: ID!
  }

  enum YesNo {
    YES
    NO
  }

  type Query {
    personCount: Int!
    /* enum for selecting people with phone */
    allPersons(phone: YesNo): [Person!]!
    findPerson(name: String!): Person
  }
`;

/* object defining how queries are responded to */
const resolvers = {
  Query: {
    personCount: () => persons.length,
    /* resolvers take root/obj, args, context, info */
    allPersons: (root, args) => {
      if (!args.phone) return persons
      const byPhone = (person) =>
        args.phone === 'YES' ? person.phone : !person.phone;
      return persons.filter(byPhone);
    },
    findPerson: (root, args) =>
      persons.find(p => p.name === args.name)
  }

  /* Apollo defines the following
     default resolvers for Person automatically*/
  Person: {
    name: (root) => root.name,
    phone: (root) => root.phone,
    street: (root) => root.street,
    city: (root) => root.city,
    id: (root) => root.id
  }

  /* need to redefine the address resolver */
  Person: {
    address: (root) => {
      return {
        street: root.street,
        city: root.city
      }
    }
  }
};

const server = new ApolloServer({
  typeDefs, resolvers
})

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`)
})
```
### Mutations
***

Operations that change the database are done with **mutations**:
```js
const typeDefs = gql`
  ...
  type Mutation {
    /* return can be null for invalid operation */
    addPerson(
      name: String!
      phone: String
      street: String!
      city: String!
    ): Person
    editNumber(
      name: String!
      phone: String!
    ): Person
  }
`

const resolvers = {
  ...
  Mutation: {
    addPerson: (root, args) => {
      /* validating unique name */
      if (person.find(p => p.name === args.name)) {
        throw new UserInputerror('Name must be unique', {
          invalidArgs: args.name
        });
      }
      const person = { ...args, id: uuid() };
      persons = persons.concat(person);
      return person;
    },
    editNumber: (root, args) => {
      const person = persons.find(p => p.name === args.name);
      if (!person) return null;
      const updatedPerson = { ...args, phone: args.phone };
      persons = person.map(p => p.name === args.name ? updatedPerson : p);
      return updatedPerson;
    }
  }
}
```
Adding a Person with the mutation:
```js
mutation {
 addPerson(
  name: "R2D2"
  street: "La Brea"
  city: "Tatooine"
 ) {
  name
  phone
  address {
    city
    street
  }
  id
 }
}
```
Saved object on the server:
```js
{
  name: "R2D2",
  street: "La Brea",
  city: "Tatooine",
  id: "123-234-123-123123"
}
```
Response to the mutation:
```js
{
  "data": {
    "addPerson": {
      "name": "R2D2",
      "phone": null,
      "address": {
        "city": "Tatooine",
        "street": "La Brea"
      },
      "id": "123-234-123-123123"
    }
  }
}
```
### Frontend
***

- GraphQL query is a string sent as value of key *query*
- higher order library instead of Axios: Relay or Apollo Client
  - Apollo Client automatically saves queries to *cache* by ID
    - as a result, new objects are not updated to state (but existing objects are)
  - to update the cache:
    - poll server repeatedly: `<Query query={ALL_PERSONS} pollInterval={2000}>`
    - synchronize queries: `<Mutation mutation={CREATE_PERSON} refetchQueries={[{ query: ALL_PERSONS }]}>`
  - to clear the cache: (eg. on logout)
    - `const client = useApolloClient()`, `client.resetStore()`
- react-apollo integrates queries with react components

Using Apollo Client and react-apollo:
```js
import ApolloClient, { gql } from 'apollo-boost';
import { ApolloProvider } from 'react-apollo;'

const client = new ApolloClient({ uri: 'https://localhost:4000/graphql' });

const query = gql`
{
  allPersons {
    name,
    phone,
    address {
      street,
      city
    },
    id
  }
}
`

client.query({ query }).then(res => console.log(res.data));

ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById('root')
);
```
Using the Query component:
```js
import { Query } from 'react-apollo';

const ALL_PERSONS = gql`
{
  allPersons {
    name,
    phone,
    id
  }
}
`

const App = () => {
  return (
    <Query query={ALL_PERSONS}>
      {(result) => <Persons result={result} />}
    </Query>
  );
}

const Persons = ({ resut }) => {
  /* as query is processing */
  if (result.loading) {
    return <div>loading...</div>;
  }

  const persons = result.data.allPersons;

  return (
    <div>
      <h2>Persons</h2>
      {persons.map(p => (
        <div key={p.name}>
          {p.name} {p.phone}
        </div>
      ))}
    </div>
  );
}
```
Using GraphQL variables for dynamic parameters:
(ApolloConsumer component gives access to the client's query method)
```js
import { Query, ApolloConsumer }

const App = () => {
  return (
    <ApolloConsumer>
      {(client) =>
        <Query ... />
      }
    </ApolloConsumer>
  );
}

const FIND_PERSON = gql`
  query findPersonByName($nameToSearch: String!) {
    findPerson(name: $nameToSearch) {
      name,
      phone,
      id,
      address{
        street,
        city
      }
    }
  }
`

const Persons = ({ result, client }) => {
  const [person, setPerson] = useState(null);
  ...
  const showPerson = async (name) => {
    const { data } = await client.query({
      query: FIND_PERSON,
      variables: { nameToSearch: name }
    });
    setPerson(data.findPerson);
  };

  if (person) {
    return (
      <div>
        <h2>{person.name}</h2>
        <div>{person.address.street} {person.address.city}</div>
        <div>{person.phone}</div>
        <button onClick={() => setPerson(null)}>close</button>
      </div>
    );
  }

  return (
    ...
    <button onClick={() => showPerson(p.name)}>show address</button>
    ...
  )
}
```
Using the Mutation component:
```js
const CREATE_PERSON = gql`
  mutation createPerson($name: String!, $street: String!, $city: String!, $phone: !string) {
    addPerson(
      name: $name,
      street: $street,
      city: $city,
      phone: $phone,
    ) {
      name,
      phone,
      id,
      address {
        street,
        city
      }
    }
  }
`

const App = () => {
  /* error handling */
  const handleError = (err) => {
    console.log(error.graphQLErrors[0].message);
  };

  return (
    ...
    <Mutation mutation={CREATE_PERSON} onError={handleError}>
      {(addPerson) => <PersonForm addPerson={addPerson}/>}
    </Mutation>
  );
}

const PersonForm = (props) => {
  ...
  const submit = async (e) => {
    e.preventDefault();
    await props.addPerson({
      variables: { name, phone, street, city }
    });
    ...
  };
}
```
#### Render-Props vs. Hooks

- the **render-props** principle:
  - where components are given a function defining how the component is rendered
  - eg. React router Route component and corresponding render function
  - eg. ApolloConsumer and Query components

Using hooks with Apollo Client:
(offered in react-apollo@3.0.0-beta.2)
```js
import { ApolloProvider } from '@apollo/react-hooks';
...
ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById('root')
);

import { useApolloClient } from '@apollo/react-hooks';

const Persons = ({ result }) => {
  const client = useApolloClient();
  ...
}

import { useQuery, useMutation } from '@apollo/react-hooks';

const App = () => {
  const persons = useQuery(ALL_PERSONS);

  /* array: mutation function, loading/error obj */
  const [addPerson] = useMutation(CREATE_PERSON, {
    onError: handleError,
    refetchQueries: [{ query: ALL_PERSONS }]
  });

  const [editNumber] = useMutation(EDIT_NUMBER);
  ...
  <Persons result={persons} />
  <PersonForm addPerson={addPerson} />
  <PhoneForm editNumber={editNumber} />
  ...
}
```
### Database
***

- to use Apollo with a *database*:
  - create a corresponding schema to the type definition
  - update the resolver definitions
    - when resolver functions return a promise, Apollo automatically sends back resolved promise

Apollo with MongoDB:
```js
const schema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true,
    minlength: 5
  },
  ...
});

module.exports = mongoose.model('Person', schema);

const typeDefs = ...

const resolvers = {
  Query: {
    personCount: () => Person.collection.countDocuments(),
    allPersons: (root, args) => {
      /* optional filter people with numbers arg */
      if (!args.phone) return Person.find({});

      return Person.find({ phone: { $exists: args.phone === 'YES' }});
    },
    findPerson: (root, args) => Person.findOne({ name: args.name })
  },
  Person: {
    address: root => {
      return {
        street: root.street,
        city: root.city
      };
    }
  },
  Mutation: {
    /* returning a promise in the resolver */
    addPerson: (root, args) => {
      const person = new Person({ ...args });

      /* validating mongoose schema */
      try {
        await person.save();
      } catch(err) {
        /* Apollo error */
        throw new UserInputError(err.message, {
          invalidArgs: args
        });
      }
      return person;
    },
    editNumber: async (root, args) => {
      const person = await Person.findOne({ name: args.name });
      person.phone = args.phone;

      try {
        await person.save();
      } catch (err) {
        throw new UserInputError(err.message, {
          invalidArgs: args
        });
      }
      return person;
    }
  }
}
```
### User Administration
***

- setting up user validation with Apollo and MongoDB in backend

Schema:
```js
/* User mongoose schema */
const schema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
    minlength: 3
  },
  friends: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Person'
    }
  ]
});
module.exports = mongoose.model('User', schema);

/* User Apollo schema */
type User {
  username: String!
  friends: [Person!]!
  id: ID!
}

type Token {
  value: String!
}

type Query {
  ...
  me: User
}

type Mutation {
  ...
  createUser(username: String!): User
  login(username: String!, password: String!): Token
}
```
Updated mutation resolvers:
```js
const resolvers = {
  Mutation {
    createUser: (root, args) => {
      const user = new User({ username: args.username });
      return user.save().catch(err => ...)
    },
    login: async (root, args) => {
      const user = await User.findOne({ username: args.username });
      if (!user || args.password !== 'pass') {
        throw new UserInputError('wrong credentials');
      const userToken = {
        username: user.username,
        id: user._id
      };
      return { value: jwt.sign(userToken, SECRET_KEY) };
    }
  }
}
```
Updated constructor and actions with context:
```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
  /* context is given to all resolver as 3rd parameter */
  /* use context for shared resolver data */
  context: async ({ req }) => {
    const auth = req ? req.headers.authorization : null;
    if (auth && auth.toLowerCase().startsWith('bearer ')) {
      const decoded = jwt.verify(auth.substring(7), SECRET_KEY);
    }
    const currentUser = await User.findById(decoded.id).populate('friends');
    return { currentUser };
  }
});

/* Query resolver */
Query: {
  ...
  me: (root, args, context) => context.currentUser
}

/* authenticated actions */
type Mutation {
  ...
  addAsFriend(name: String!): User
}

addAsFriend: aync (root, args, { currentUser }) => {
  const nonFriendAlready = (person) =>
    !currentUser.friends.map(f => f._id).includes(person._id);

  if (!currentUser) {
    throw new AuthenticationError("not authenticated");
  }

  const person = await Person.findOne({ name: args.name });
  if (nonFriendAlready(person)) {
    currentUser.friends = currentUser.frieds.concat(person);
  }

  await currentUser.save();
  return currentUser;
}
```
### User Administration on the Frontend
***

Saving token on login success:
```js
const LoginForm = (props) => {
  ...
  const submit = async (e) => {
    e.preventDefault();

    const res = await props.login({ variables: { username, password }});

    if (res) {
      const token = res.data.login.value;
      /* saved in root App component */
      props.setToken(token);
      /* saved in local storage */
      localStorage.setItem('phonenumbers-user-token', token);
    }
  };
  ...
}
```
Clearing storage and cache on logout:
```js
const App = () => {
  const client = useApolloClient();
  ...
  const logout = () => {
    setToken(null);
    localStorage.clear();
    client.resetStore();
  };
  ...
}
```
Automatically adding tokens to headers:
```js
/* using apollo-client instead of apollo-boost for custom configuration */
import { ApolloClient } from 'apollo-client';
import { createHttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { setContext } from 'apollo-link-context';

const httpLink = createHttpLink({ uri: ... });

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('phonenumbers-user-token');
  return {
    headers: {
      ...headers,
      authorization: token ? `bearer ${token}` : null
    }
  };
});

const client = new ApolloClient({
  /* how client contacts the server */
  /* httpLink and custom token in header */
  link: authLink.concat(httpLink),
  /* using cache in main memory */
  cache: new InMemoryCache()
});
```
Alternative for updating cache:
```js
const [addPerson] = useMutation(CREATE_PERSON, {
  onError: handleError,

  /* query always rerun with any updates */
  /* refetchQueries: [{ query: ALL_PERSONS }] */

  /* manually updating cache */
  update: (store, res) => {
    const dataInStore = store.readQuery({ query: ALL_PERSONS });
    dataInStore.allPersons.push(res.data.addPerson);
    store.writeQuery({
      query: ALL_PERSONS,
      data: dataInStore
    });
  }
})
```
### Fragments and Subscriptions
***

- often useful to define **fragments** for selecting fields
  - fragments are defined in the client, *not* the GraphQL schema itself

Using fragments to automatically grab all fields:
```js
const PERSON_DETAILS = gql`
  fragment PersonDetails on Person {
    id
    name
    phone
    address {
      street
      city
    }
  }
`

const ALL_PERSONS = gql`
  {
    allPersons {
      ...PersonDetails
    }
  }
  ${PERSON_DETAILS}
`
```
- GraphQL **subscription** is another operation type (query, mutation)
  - clients can *subscribe* to changes in the server
  - under the hood, Apollo uses WebSockets for this subscriptions
- communication uses the *publish-subscribe* principle with a PubSub interface:
  - adding a new object *publishes* a notification about the operation with `publish`
  - the subscription resolver registers all subscribers by returning them an *iterator* object

- the *n+1* problem appears in database querying:
  - when attempting to load the children of a parent relationship
  - querying the database repeatedly, n+1 times
- solution usually involves using join queries:
  - eg. can use MongoDB join query to populate child fields
  - check query info to only do join queries for n+1 problem queries
    - minimizes execution when query does not raise an n+1 problem

Setting up subscriptions on the server:
```js
/* updated schema: */
type Subscription {
  /* when a new person is added, */
  /* its details are sent to all subscribers */
  personAdded: Person!
}

/* updated resolvers: */
const { PubSub } = require('apollo-server');
const pubsub = new PubSub();

const resolvers = {
  ...
  Mutation: {
    addPerson: async (root, args, context) => {
      ...
      pubsub.publish('PERSON_ADDED', { personAdded: person });
      return person;
    }
  },
  Subscription: {
    personAdded: {
      subscribe: () => pubsub.asyncIterator(['PERSON_ADDED'])
    }
  }
}

/* updated server start to listen for subscriptions: */
server.listen().then(({ url, subscriptionsUrl }) => {
  console.log(`Server ready at ${url}`);
  /* different url */
  console.log(`Subscriptions ready at ${subscriptionsUrl}`);
})
```
Using subscriptions on the frontend:
(requires subscriptions-transport-ws and apollo-link-ws)
```js
import { split } from 'apollo-link';
import { WebSocketLink } from 'apollo-link-ws';
import { getMainDefinition } from 'apollo-utilities';

/* requires websocket as well as HTTP connection */
const wsLink = new WebSocketLink({
  uri: ...,
  options: { reconnect: true }
});

...

const link = splilt(
  /* splits to different link depending on operation */
  ({ query }) => {
    const { kind, operation } = getMainDefinition(query);
    return kind === 'OperationDefinition' && operation === 'subscription';
  },
  wsLink,
  authLink.concat(httpLink)
);

const client = new ApolloClient({
  link,
  cache: new InMemoryCache()
});
```
Using subscriptions with hooks:
```js
import { useSubscription } from '@apollo/react-hooks';

const PERSON_ADDED = gql`
  subscription {
    personAdded {
      ...PersonDetails
    }
  }
  ${PERSON_DETAILS}
`;

const App = () => {
  ...
  useSubscription(PERSON_ADDED, {
    onSubscripionData: ({ subscriptionData } => {
      console.log(subscriptionData);
    })
  })
  ...
}
```
Updating cache with subscription:
```js
const App = () => {
  ...
  const updateCacheWith = (addedPerson) => {
    const includedIn = (set, object) => {
      set.map(p => p.id).includes(object.id);
    }

    const dataInStore = client.readQuery({ query: ALL_PERSONS });
    if (!includedIn(dataInStore.allPersons, addedPerson)) {
      dataInStore.allPersons.push(addedPerson);
      client.writeQuery({
        query: ALL_PERSONS,
        data: dataInStore
      });
    }
  };

  useSubscription(PERSON_ADDED, {
    onSubscripionData: ({ subscriptionData }) => {
      const addedPerson = subscriptionData.data.personAdded;
      notify(`${addedPerson.name} added`);
      updateCacheWith(addedPerson);
    }
  });

  const [addPerson] = useMutation(CREATE_PERSON, {
    onError: handleError,
    update: (store, res) => {
      updateCacheWith(res.data.addPerson);
    }
  });
  ...
}
```
