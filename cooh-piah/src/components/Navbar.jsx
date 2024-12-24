import React from 'react'

const Navbar = () => {
  return (
    <div>
      <div className='bg-gradient-to-r from-blue-200 to-blue-700 w-full sm:h-[8vw] md:h-[8vw] lg:h-[8vw] flex items-center justify-center'>
        <p className='font-nunito md:font-roboto text-gray-1000 bold font-semibold text-2xl'>
            Bem vindo ao Plagiador CoOh-Piah
        </p>
    </div>
    {/* input dos textos */}
    <div className='flex justify-between items-start mt-20 px-20'>
  {/* Primeira Div */}
  <div className='rounded-2xl bg-indigo-500 p-6 shadow-lg flex flex-col items-center ml-60'>
    <p className='text-white font-semibold mb-4'>Texto 1</p>
    <form action="">
      <label htmlFor="text1" className='text-white block mb-2'>Digite o primeiro texto:</label>
      <input
        id="text1"
        type="text"
        className='rounded p-2 w-full border focus:outline-none focus:ring-2 focus:ring-indigo-300'
        placeholder="Digite aqui..."
      />
    </form>
  </div>

  {/* Segunda Div */}
  <div className='rounded-2xl bg-indigo-500 p-6 shadow-lg flex flex-col items-center mr-60'>
    <p className='text-white font-semibold mb-4'>Texto 2</p>
    <form action="">
      <label htmlFor="text2" className='text-white block mb-2'>Digite o segundo texto:</label>
      <input
        id="text2"
        type="text"
        className='rounded p-2 w-full border focus:outline-none focus:ring-2 focus:ring-indigo-300'
        placeholder="Digite aqui..."
      />
    </form>
  </div>
</div>

  
  </div>
  
    
  )
}

export default Navbar