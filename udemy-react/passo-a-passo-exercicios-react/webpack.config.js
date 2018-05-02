const webpack = require('webpack')

module.exports = {
  entry: './ex/index.jsx',
  output: {
    path: __dirname + '/public',
    filename: './bundle.js'
  },//output
  devServer: {
    port: 8080,
    contentBase:'./public',
  },//devServer
  resolve: {
    extensions: ['', '.js', '.jsx']
  },//resolve
  module:{
    loaders: [{
      test: /.jsx?$/,
      loader: 'babel-loader',
      exclude: /node_modules/,
      query:{
        presets: ['es2015', 'react']
      }//query
    }]//loaders
  }//module
}//module.exports
