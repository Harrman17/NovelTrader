import React from 'react'
import { Link } from 'react-router-dom'

function Header() {

  return (
    <div className='flex h-17 bg-gray-50 px-3 items-center'>
        <h1 className='font-bold font-mono p-5 text-xl text-main'>NOVELTRADER</h1>
        <Link to="list-a-car" className="ml-auto">
          <button className="bg-accent text-white text-sm rounded-lg w-25 h-9 ml-auto sm:h-10 sm:text-md sm:w-30">List your car</button>
        </Link>
    </div>
  )
}

export default Header