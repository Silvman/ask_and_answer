var path = require('path');
let webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
	  entry: {
		  main: './js/index.js',
		  style: './css/custom.scss'
	  },

	  output: {
		  filename: '[name].bundle.js',
		  path: path.resolve(__dirname, 'static')
	  },

    resolve: {
        modules: [
          "node_modules"
        ]
      },

	  module: {
          loaders: [
              {
                test: /\.(scss)$/,
                use: ExtractTextPlugin.extract({
                    fallback:  'style-loader',
                    use: [ {
                  loader: 'css-loader', // translates CSS into CommonJS modules
                }, {
                  loader: 'postcss-loader', // Run post css actions
                  options: {
                    plugins: function () { // post css plugins, can be exported to postcss.config.js
                      return [
                        require('precss'),
                        require('autoprefixer')
                      ];
                    }
                  }
                }, {
                  loader: 'sass-loader' // compiles Sass to CSS
                }]
})
              },

              {
         test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
         use: [{
           loader: 'file-loader',
           options: {
             name: '[name].[ext]',
             outputPath: 'fonts/',    // where the fonts will go
             publicPath: '/static/fonts'       // override the default path
           }
         }]
       },
          ]
      },

	  plugins: [
		new ExtractTextPlugin({
			filename: "style.bundle.css"
		}),

		new webpack.DefinePlugin({
      'process.env': {
        // This has effect on the react lib size
        'NODE_ENV': JSON.stringify('production'),
      }
    }),
/*
    new webpack.optimize.AggressiveMergingPlugin(),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({
      mangle: true,
      compress: {
        warnings: false, // Suppress uglification warnings
        pure_getters: true,
        unsafe: true,
        unsafe_comps: true,
        screw_ie8: true
      },
      output: {
        comments: false,
      },
      exclude: [/\.min\.js$/gi] // skip pre-minified libs
    }),
          */
	]
};
