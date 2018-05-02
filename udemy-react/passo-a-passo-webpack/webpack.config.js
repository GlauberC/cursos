const webpack = require('webpack')
const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  entry: './ex/index.js',
  output:{
    path: __dirname + '/public',
    filename: './bundle.js'
  },//output
  devServer: {
    port: 8080,
    contentBase: './public'
  },//devServer
  plugins: [
    new ExtractTextPlugin('app.css')
  ],//plugins
  module: {
    loaders: [{
      test:/.js?$/,
      loader: 'babel-loader',
      exclude: /node_modules/,
      query:{
        presets: ['es2015', 'react'],
        plugins: ['transform-object-rest-spread']
      }//query
    }, {
      test: /\.css$/,
      loader: ExtractTextPlugin.extract("style-loader", "css-loader")
    }]//test loaders
  }//module
}//module.exports
