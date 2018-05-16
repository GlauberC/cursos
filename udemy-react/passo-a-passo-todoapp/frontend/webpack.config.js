const webpack = require('webpack')
const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports={
  entry: './src/index.jsx',
  output: {
    path: __dirname + '/public',
    filename: './app.js'
  },//output
  devServer: {
    port:8080,
    contentBase: './public',

  },//devServer
  resolve: {
    extensions: ['', '.js', '.jsx'],
    alias: {
      modules: __dirname + '/node_modules'
    }//alias
  },//resolve
  plugins: [
    new ExtractTextPlugin('app.css')
  ],//plugins
  module: {
    loaders: [{
      test: /.js[x]?$/,
      loader: 'babel-loader',
      exclude: /node_modules/,
      query:{
        presets: ['es2015', 'react'],
        plugins: ['transform-object-rest-spread']
      }//query
    },//loaderJS
    {
      test:/\.css$/,
      loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
    },//loaderCSS
    {
      test: /\.woff|.woff2|.ttf|.eot|.svg*.*$/,
      loader: 'file'
    }//loaderTemplates
    ]//loaders
  }//module
}//module.exports
