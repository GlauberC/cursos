import ReactDOM from 'react-dom'
import React from 'react'
import ClassComponent from './classComponent'

ReactDOM.render(
  <ClassComponent label='Contador' initialValue={10}/>
  ,document.getElementById('app'))
