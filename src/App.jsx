import { useState, useRef } from 'react'
import Header from './components/Header'
import Search from './components/Search'
import Landing from './components/Landing'
import ListCar from './components/ListCar'
import { Routes, Route } from 'react-router-dom'


function App() {
  const searchRef = useRef(null)

  return (
    // main page / landing

    <div>
        <Routes>
          <Route path="/" element={
          <>
            <Header />
            <Landing onFindClick={() => searchRef.current.scrollIntoView({ behavior: "smooth" })}/>
            <div ref={searchRef}>
              <Search />
            </div>
          </>}/>
          <Route path="list-a-car" element={
            <>
              <ListCar />
            </>}/>
        </Routes>
    </div>

  )
}

export default App
