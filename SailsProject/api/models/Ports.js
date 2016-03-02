/**
 * Ports.js
 *
 * @description :: TODO: You might write a short summary of how this model works and what it represents here.
 * @docs        :: http://sailsjs.org/documentation/concepts/models-and-orm/models
 */

module.exports = {

  attributes: {

    source_port: {
      type:'integer',
      required: true
    },

    dest_ip: {
      type:'string',
      required: true
    },

    dest_port:{
      type:'integer',
      required: true
    }

  }
};

