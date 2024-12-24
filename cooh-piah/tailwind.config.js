/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily:{
        sans: ['Roboto','sans-serif',''],
        'nunito': ['nunito-sans']
      },
      gridTemplateColumns: {
        '70/30': '70% 28%'
      },
      colors:{
        'blue':{
          100 : '#dbeafe',
          200 : '#bfdbfe',
          300 : '#93c5fd',
          400 : '#3b82f6',
          500 : '#2563eb',
          600 : '#2563eb',
          700 : '#1d4ed8'
        },
        'indigo':{
          400 : '#818cf8',
          500 : '#6366f1',
          600 : '#4f46e5'
        }
      },
      fontWeight:{
        normal: '400',
        medium: '500',
        semibold:'600',
        bold: '700'
      }
    },
  },
  plugins: [],
}

