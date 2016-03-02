/**
 * PortsController
 *
 * @description :: Server-side logic for managing ports
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

module.exports = {

  'new': function (req, res) {
    res.view();
  },

  create: function(req, res) {
    Ports.create(req.params.all(), function PortCreated (err, port) {
      if (err) {
        next(err);
        return res.redirect('/Ports/new');
      }
      res.redirect('/Ports/index');
    });
  },

  index: function (req,res,next) {
    Ports.find(function foundPorts (err, ports) {
      if (err) return next(err);
      res.view({
        ports: ports
      });
    });
  },

  destroy: function (req, res) {
    Ports.destroy(req.params.all(), function PortsDestroyed (err, port) {
      if (err) return next(err);
      res.redirect('/Ports/index');
    });
  },

  refresh: function (req, res) {
    if (sails.config.myconf.pythonChild != 65535) {
      sails.config.myconf.pythonChild.kill();
    }
    var spawn = require("child_process").spawn;
    sails.config.myconf.pythonChild = spawn('python',["/root/.test/COMP8005_Assignment3_PortForwarding/BrokenRouter/forwarder.py"]);
    res.redirect('/Ports/index');
  }

};

