/**
 * Ports.js
 *
 * @description :: TODO: You might write a short summary of how this model works and what it represents here.
 * @docs        :: http://sailsjs.org/documentation/concepts/models-and-orm/models
 */

module.exports = {

  attributes: {

    source_ip: {
      type:'string',
      required: true
    },

    source_port: {
      type:'integer',
      required: true,
      unique: true
    },

    dest_ip: {
      type:'string',
      required: true
    },

    dest_port:{
      type:'integer',
      required: true,
      unique: true
    }

  }
};

