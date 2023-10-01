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
        'exsm':{"max":'460px'},
      }
    },
  },
  plugins: [],
}

