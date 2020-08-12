const THEMES = {
  cool_fresh: {
    text_secondary: "#05386b",
    accent_dark: "#379683",
    primary: "#5cdb95",
    accent_light: "#8ee4af",
    text_primary: "#edf5e1"
  }
}

// ENTER THEME NAME HERE:
const THEME = THEMES.cool_fresh

const COLORS = {
  PRIMARY: THEME.primary,
  TEXT_PRIMARY: THEME.text_primary,
  TEXT_SECONDARY: THEME.text_secondary,
  ACCENT_DARK: THEME.accent_dark,
  ACCENT_LIGHT: THEME.accent_light
}

module.exports = {
  purge: [],
  theme: {
    colors: {
      text_secondary: COLORS.TEXT_SECONDARY,
      accent_dark: COLORS.ACCENT_DARK,
      primary: COLORS.PRIMARY,
      accent_light: COLORS.ACCENT_LIGHT,
      text_primary: COLORS.TEXT_PRIMARY
    }
  },
  extend: {},
  variants: {
    text: ['responsive', 'hover', 'focus', 'active', 'group-hover']
  }
}
