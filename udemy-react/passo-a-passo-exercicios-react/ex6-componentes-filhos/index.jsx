import React from 'react'
import ReactDOM from 'react-dom'
import Family from './family'
import Member from './member'

ReactDOM.render(
  <Family>
    <Member name='Fulaninho' lastName='da Silva'/>
    <Member name='Fulana' lastName='da Silva'/>
  </Family>
, document.getElementById('app'))
