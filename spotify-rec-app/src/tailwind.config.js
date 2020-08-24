const THEMES = {
  cool_fresh: {
    c5: "#05386b",
    c4: "#379683",
    c3: "#5cdb95",
    c2: "#8ee4af",
    c1: "#edf5e1"
  },
  something_else: {
      text_secondary: "#05386b",
      accent_dark: "#379683",
      primary: "orange",
      accent_light: "#8ee4af",
      text_primary: "#edf5e1"
    }
}

// ENTER THEME NAME HERE:
const THEME = THEMES.cool_fresh

module.exports = {
  purge: [],
  theme: {
    colors: {
      c1: THEME.c1,
      c2: THEME.c2,
      c3: THEME.c3,
      c4: THEME.c4,
      c5: THEME.c5
    },
    fill: {
    
    }
  },
  extend: {
    animation: {
      'spin-slow': 'spin 3s linear infinite',
    }
  },
  variants: {
    text: ['responsive', 'hover', 'focus', 'active', 'group-hover'],
    animation: ['responsive', 'motion-safe', 'motion-reduce']
  }
}
