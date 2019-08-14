# Full Stack Course
***

## 5. Front-End Testing and Custom Hooks
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
## 6. Redux
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
## 7. React Router and Styling
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
