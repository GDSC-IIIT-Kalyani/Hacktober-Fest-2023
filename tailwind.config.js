/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./dist/*.{html,js}"],
  theme: {
    extend: {
      fontFamily:{
        "jetbrains":["JetBrains Mono",'monospace']
      },
      screens:{
        'extrasmall':{"max":'593px'},
      }
    },
  },
  plugins: [],
}

