# Responsive Web Design
***

- a *responsive site* responds to different devices
  - eg. both desktop and mobile devices
  - *breakpoints* controls how website looks at different widths
- **viewport** is the width of the website on different devices
  - default behavior is to simply "squish" the desktop width
  - should override the default viewport to make it thinner
```html
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- setting the viewport to the device width -->
</head>
```
- **media queries** allow us to create CSS rules based on various parameters
  - eg. viewport size, device type, etc
  - syntax: `@media <media-type> and (expressions) {}`
    - eg. `@media TV and (min-width: 1200px) {}`
```css
@media screen and (max-width: 700px) { /* this is a new breakpoint */
  #featured li {
    width: 45%;
  }
}
```

