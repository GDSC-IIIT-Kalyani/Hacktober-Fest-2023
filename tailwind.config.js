/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./dist/*.{html,js}"],
  theme: {
    extend: {
      flex: {
        '6': '6',
        '3': '3',
        '5': '5',
      },
      colors:{
      "black01":"#0F0913",
      gold1:"#F9CB33",
      vuejs:"#49e659"
    },
    size:{
      'rl':"200rem",
      1:"1%",
      '9/10':"90%"
    },
    boxShadow:{
      custom:" 0 0 1px 1px #FFFBA4"},
    fontFamily:{
      Jetbrains: ['JetBrains Mono', 'monospace']
    },
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

