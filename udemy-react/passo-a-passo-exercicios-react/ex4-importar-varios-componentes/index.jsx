import React from 'react'
import ReactDOM from 'react-dom'
import {Primeiro, Segundo} from './component'

//O react exige uma tag para agrupar mais de um component
ReactDOM.render(
  <div>
    <Primeiro/>
    <Segundo/>
  </div>

  , document.getElementById('app'))
