/** Tailwind build config. Rebuild the stylesheet with:
 *  npx tailwindcss@3.4.17 -i tools/tailwind.input.css -o assets/tailwind.css --minify
 */
module.exports = {
  content: ['./index.html', './404.html', './services/*.html', './assets/*.js', './tools/*.py'],
  theme: {
    extend: {
      colors: {
        ink: '#0A0A0F',
        muted: '#55576A',
        line: '#E6E6EF',
        surface: '#F7F7FB',
        brand: { DEFAULT: '#554DF1', dark: '#3F37D6', soft: '#EEEDFE' },
        sky: { DEFAULT: '#0091E0', dark: '#0070AD', soft: '#E3F3FC' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
      },
      maxWidth: { site: '1200px' },
    },
  },
};
