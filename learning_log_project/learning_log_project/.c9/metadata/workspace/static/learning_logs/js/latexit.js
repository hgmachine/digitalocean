{"filter":false,"title":"latexit.js","tooltip":"/static/learning_logs/js/latexit.js","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":109,"column":17},"end":{"row":109,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"7991c5f46d1a7fc2410e886b5201fd0339872ca6","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":109,"column":17},"action":"insert","lines":["/*","* LaTeX IT - JavaScript to Convert Latex within an HTML page into Equations","* Copyright (C) 2009 William Bateman, 2008 Waipot Ngamsaad ","","* This program is free software: you can redistribute it and/or modify","* it under the terms of the GNU General Public License as published by","* the Free Software Foundation, either version 3 of the License, or","* (at your option) any later version.","","* This program is distributed in the hope that it will be useful,","* but WITHOUT ANY WARRANTY; without even the implied warranty of","* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the","* GNU General Public License for more details.","","* You should have received a copy of the GNU General Public License","* along with this program.  If not, see <http://www.gnu.org/licenses/>.","*/","","var LatexIT = {","\tmode : 'gif',","\timgnum : 0,","\tisFirefox:false,","\tinit : function() {","\t\t// We need to review the support for SVG. Latest released versions are not supporting this as they should","  //  if(document.implementation.hasFeature(\"http://www.w3.org/TR/SVG11/feature#BasicStructure\", \"1.1\"))","\t//\t  this.mode='svg';","","    // browser name","\t\t// svg support in FireFox is not allowing two images to occur currently on the same line. ","\t\t","\t\tvar ua = navigator.userAgent.toLowerCase(); ","\t\tif(ua.indexOf(\"firefox\")!=-1)","\t\t{","      // this.isFirefox = true;","\t\t}","  },","","\tpre : function(txt) {","\t\tif ( !txt.match(/<img.*?>/i) )","\t\t{","\t\t\t//Clean code","\t\t\ttxt=txt.replace(/<br>/mgi,\"\");","\t\t\ttxt=txt.replace(/<br \\/>/mgi,\"\");","\t\t\t//Create img tag","\t\t//\ttxt = \" <img src=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" /> \";","\t\t//\ttxt = \" <object type=\\\"image/svg+xml\\\" width=\\\"20\\\" data=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" /> \";","\t\t  ","\t\t  if(this.mode=='svg')  ","\t\t\t{","\t\t\t\t// Best for Firefox","\t\t\t\tif(this.isFirefox) ","  \t\t   \ttxt = \" <object type=\\\"image/svg+xml\\\" data=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" class=\\\"latex\\\" style=\\\"margin:0; padding:0; border:0\\\" /> \";","\t\t\t\telse // Best for Chrome","  \t\t   //\ttxt = \" <object type=\\\"image/svg+xml\\\" data=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" class=\\\"latex\\\" /> \";","\t\t\t\t\ttxt = \" <img src=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" alt=\\\"\"+ txt +\"\\\" title=\\\"\"+ txt +\"\\\" border=\\\"0\\\" class=\\\"latex\\\" /> \";","\t\t\t}","\t\t\telse ","\t   \t  txt = \" <img src=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\"+ txt +\"\\\" alt=\\\"\"+txt+\"\\\" border=\\\"0\\\" class=\\\"latex\\\" /> \";","\t\t}","\t\treturn txt;","\t},","\t","\tlatex : function(txt) {","\t\tvar html, htmlinline;","\t\tif(this.isFirefox) {","\t\t  html=\" <object type=\\\"image/svg+xml\\\" data=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?$2\\\" class=\\\"latex\\\" /> \";","\t\t  htmlinline=\" <object type=\\\"image/svg+xml\\\" data=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\\\\inline $2\\\" class=\\\"latex\\\" /> \";","\t\t}","\t\telse {","\t\t  html=\" <img src=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?$2\\\" border=\\\"0\\\" class=\\\"latex\\\" /> \";","\t\t  htmlinline=\" <img src=\\\"http://latex.codecogs.com/\"+this.mode+\".latex?\\\\inline $2\\\" border=\\\"0\\\" class=\\\"latex\\\" /> \";","\t\t}","\t","\t","\t  txt=txt.replace(/(^\\$|[^\\\\]\\$)(.*?[^\\\\])\\$/gm, htmlinline);","\t\ttxt=txt.replace(/(^\\\\|[^\\\\]\\\\)\\[(.*?[^\\\\])\\\\\\]/mg,\" <br/>\"+html+\"<br/> \"); ","\t\ttxt=txt.replace(/\\\\\\$/mg,\"\\$\"); ","\t\ttxt=txt.replace(/\\\\\\\\(\\[|\\])/mg,\"$1\");","\t\t","\t\treturn txt;","\t},\t","\t","\trender : function(tag, latexmode) {","\t\tvar eqn = window.document.getElementsByTagName(tag);","\t\tfor (var i=0; i<eqn.length; i++) {","\t\t\tif(latexmode)","\t\t\t  eqn[i].innerHTML = LatexIT.latex(eqn[i].innerHTML);","\t\t\telse if (eqn[i].getAttribute(\"lang\") == \"latex\" || eqn[i].getAttribute(\"xml:lang\") == \"latex\") ","\t\t\t  eqn[i].innerHTML = LatexIT.pre(eqn[i].innerHTML);","\t\t} ","\t},","","  add : function(tag, latexmode)","\t{","\t\tif(typeof(latexmode)=='undefined') latexmode=false; ","\t\tif(window.addEventListener) ","\t\t\twindow.addEventListener('load', new Function('LatexIT.render(\"'+tag+'\", '+latexmode+')'),false);","\t\telse ","\t\t  window.attachEvent('onload', new Function('LatexIT.render(\"'+tag+'\", '+latexmode+')') );","\t},","","\tscale : function(e,scale)","\t{","\t\te.width =(e.width*scale);","\t\te.height=(e.height*scale);","\t}","};","","LatexIT.init();","LatexIT.add('*');"],"id":1}]]},"timestamp":1572376964953}