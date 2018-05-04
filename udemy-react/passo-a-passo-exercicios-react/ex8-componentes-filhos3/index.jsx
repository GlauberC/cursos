import React from 'react'
import ReactDOM from 'react-dom'
import Family from './family'
import Member from './member'

ReactDOM.render(
  <div>
    <Family lastName='da Silva'>
      <Member name='Fulaninho'/>
      <Member name='Fulana'/>
      <Member name='Fulinha'/>
    </Family>
    <Family lastName='Lima'>
      <Member name='Sicrano'/>
      <Member name='Sicraninha'/>
    </Family>
  </div>
, document.getElementById('app'))
