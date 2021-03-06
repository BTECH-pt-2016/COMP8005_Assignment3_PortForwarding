/**
 * Bootstrap
 * (sails.config.bootstrap)
 *
 * An asynchronous bootstrap function that runs before your Sails app gets lifted.
 * This gives you an opportunity to set up your data model, run jobs, or perform some special logic.
 *
 * For more information on bootstrapping your app, check out:
 * http://sailsjs.org/#!/documentation/reference/sails.config/sails.config.bootstrap.html
 */

module.exports.bootstrap = function(cb) {
  sails.on('lifted', function() {
    if (sails.config.myconf.pythonChild != 65535) {
      sails.config.myconf.pythonChild.kill();
    }
    var spawn = require("child_process").spawn;
    sails.config.myconf.pythonChild = spawn('python',["/root/.test/COMP8005_Assignment3_PortForwarding/BrokenRouter/forwarder.py"]);
  });
  // It's very important to trigger this callback method when you are finished
  // with the bootstrap!  (otherwise your server will never lift, since it's waiting on the bootstrap)
  cb();
};
