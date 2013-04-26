// Todo: clean up MapAsset events and get draw_markers/render_table events
// in sync. Possibly move MapBlacklist into it's own collection and listen
// for change events.

IONUX.DashboardView = "Map";

IONUX.Views.ViewControls = Backbone.View.extend({
  el: '#view-controls',
  dashboard_template: _.template($('#dashboard-content-tmpl').html()),
  events: {
    'click #btn-map': 'render_map_view',
    'click #btn-resources': 'render_list_view'
  },
  initialize: function(){
    _.bindAll(this);
  },
  render: function() {
    this.$el.show();
    return this;
  },  
  render_map_view: function(e) {
    if (e) e.preventDefault();
    $('#btn-map').addClass('active').siblings('.active').removeClass('active');
    IONUX.ROUTER.navigate('/', true);
  },
  render_list_view: function(e) {
    if (e) e.preventDefault();
    $('#btn-resources').addClass('active').siblings('.active').removeClass('active');
    IONUX.ROUTER.navigate('/resources', true);
  },
});


/* 
- - - - - - - - - - - - - - - - - 
  Site Navigation
- - - - - - - - - - - - - - - - - 
*/

IONUX.Collections.Orgs = Backbone.Collection.extend({
  url: '/Org/list/',
  parse: function(resp) {
    // console.log('Orgs', resp);
    return resp.data;
  }
});

IONUX.Collections.Observatories = Backbone.Collection.extend({
  url: '/Observatory/list/',
  parse: function(resp) {
    return resp.data;
  }
});

IONUX.Views.ResourceSelector = Backbone.View.extend({
  el: '#resource-selector',
  initialize: function(){
    _.bindAll(this);
    this.title = this.options.title;
    this.collection.on('reset', this.render);
  },
  render: function(){
    this.$el.removeClass('placeholder');
    this.$el.show().html(this.template({resources: this.collection.toJSON(), title: this.title}));
    return this;
  },
});

IONUX.Views.ObservatorySelector = IONUX.Views.ResourceSelector.extend({
  template: _.template($('#dashboard-observatory-list-tmpl').html()),
  
  events: {
    'click .map-ul > li a.primary-link': 'spatial_area_name'
  }, 

  initialize: function(){
    _.bindAll(this);
    this.title = this.options.title;
    this.collection.on('reset', this.render);
  },

  render: function(){
    this.$el.removeClass('placeholder');
    this.$el.show().html(this.template({resources: this.build_menu(), title: this.title}));
    return this;
  },
  
  build_menu: function(){
    // Grab all spatial names, then uniques; separate for clarity.
    var spatial_area_names = _.map(this.collection.models, function(resource) {
      var san = resource.get('spatial_area_name');
      if (san != '') return san;
    });
    var unique_spatial_area_names = _.uniq(spatial_area_names);
    
    var resource_list = {};
    _.each(unique_spatial_area_names, function(san) {
      resource_list[san] = _.map(this.collection.where({spatial_area_name: san}), function(resource) { return resource.toJSON()});
    }, this);
    return resource_list;
  },
  
  spatial_area_name: function(e){
    // Todo: catching clicks until panning to children geo bounds is implemented
    e.preventDefault();
    return false;
  },
});

IONUX.Views.OrgSelector = IONUX.Views.ResourceSelector.extend({
  template: _.template($('#dashboard-org-list-tmpl').html()),
});


/* 
- - - - - - - - - - - - - - - - - 
  Asset Map
- - - - - - - - - - - - - - - - - 
*/

IONUX.Models.MapResource = Backbone.Model.extend({
  defaults: {
    geospatial_point_center: {
      lat: 39.8106460,
      lon: -98.5569760
    },
    constraint_list: null
  }
});

IONUX.Collections.MapResources = Backbone.Collection.extend({
  initialize: function(models, options){
    this.resource_id = options.resource_id;
  },
  url: function() {
   return '/related_sites/'+this.resource_id+'/';
  },
  parse: function(resp) {
    var related_sites = [];
    _.each(resp.data, function(site){related_sites.push(site)});
    return related_sites;
  }
});

IONUX.Views.Map = Backbone.View.extend({
  el: '#map_canvas',
  initialize: function(){
    _.bindAll(this);
    this.active_marker = null; // Track clicked icon
    this.draw_map();
    this.model.on('pan:map', this.pan_map);
    // this.collection.on('reset', this.draw_markers);
    // this.collection.on('reset', this.render_table);
  },

  render: function(){
    this.$el.show();
    return this;
  },
  
  draw_map: function(map_options, container_server) {
    console.log('draw_map');
    $('#map_canvas').empty().show();
    this.map = new google.maps.Map(document.getElementById('map_canvas'), {
      center: new google.maps.LatLng(39.8106460, -98.5569760),
      zoom: 3,
      mapTypeId: google.maps.MapTypeId.TERRAIN,
      disableDefaultUI: true,
      // scrollwheel: false,
    });
    this.markerClusterer = new MarkerClusterer(this.map, null, {
      maxZoom: 10, 
      // styles: {
      //   backgroundPosition: '-430px -1px',
      //   height: 60,
      //   width: 60,
      //   url: 'http://localhost:3000/static/img/sprite.png'
      // }
    });
    this.pan_map();
    this.draw_markers();
  },
  
  draw_markers: function() {
    console.log('draw_markers');
    var self = this;
    _.each(this.collection.models, function(resource) {
      var lat = resource.get('geospatial_point_center')['lat'];
      var lon = resource.get('geospatial_point_center')['lon'];
      // console.log('lat', lat, 'lon', lon);

      var rid = resource.get('_id');
      var rname = resource.get('name');
      self.create_marker(lat, lon, null, rname,"<P>Insert HTML here.</P>", null, rid);
    });    
  },
  
  pan_map: function() {
    console.log('pan_map');
    try {
      var n = this.model.get('constraint_list')[0]['geospatial_latitude_limit_north'];
      var e = this.model.get('constraint_list')[0]['geospatial_longitude_limit_east'];
      var s = this.model.get('constraint_list')[0]['geospatial_latitude_limit_south'];
      var w = this.model.get('constraint_list')[0]['geospatial_longitude_limit_west'];
      var ne = new google.maps.LatLng(n, e);
      var sw = new google.maps.LatLng(s, w);
      var bounds = new google.maps.LatLngBounds(sw, ne)
      this.map.fitBounds(bounds);
    } catch(err) {
      console.log('pan_map error:', err);
    }
  },
  
  create_marker: function(_lat, _lon, _icon, _hover_text, _info_content, _table_row, resource_id) {
    if (!_lat || !_lon) return null;

    // Once we get status in find_related, these will be
    // moved into their own dictionary.
    var sprite_url = '/static/img/sprite.png'
    var na_icon = {
        anchor: new google.maps.Point(30, 30),
        origin: new google.maps.Point(420, 180),
        size: new google.maps.Size(60, 60),
        url: sprite_url
    };
    var na_icon_hover = {
      anchor: new google.maps.Point(30, 30),
      origin: new google.maps.Point(480, 180),
      size: new google.maps.Size(60, 60),
      url: sprite_url
    };
    var na_icon_active = {
        anchor: new google.maps.Point(30, 30),
        origin: new google.maps.Point(540, 180),
        size: new google.maps.Size(60, 60),
        url: sprite_url
    };
    latLng = new google.maps.LatLng(_lat, _lon);
    var marker = new google.maps.Marker({
      map: this.map,
      position: latLng,
      icon: na_icon,
      title: _hover_text,
      resource_id: resource_id
    });
    
    var iw = new google.maps.InfoWindow({content: _info_content});
    var _map = this.map;
    
    // Event when marker is clicked
    var self = this;
    google.maps.event.addListener(marker, 'click', function(_map) {
      // iw.open(this.map, marker);
      
      if (self.active_marker) self.active_marker.setIcon(na_icon);
      marker.setIcon(na_icon_active);
      self.active_marker = marker;
      if (typeof marker.resource_id != 'undefined') {
        IONUX.ROUTER.navigate('/map/'+marker.resource_id, {trigger:true});
      };
    });

    // Event for mouseover
    google.maps.event.addListener(marker, 'mouseover', function() {
      // _table_row.style.backgroundColor = _row_highlight_color;
      if (marker.icon !== na_icon_active) {
        marker.setIcon(na_icon_hover);
      };
    });
    
    // Event for mouseout
    google.maps.event.addListener(marker, 'mouseout', function() {
      // _table_row.style.backgroundColor = _row_background_color;
      if (marker.icon !== na_icon_active) {
        marker.setIcon(na_icon);
      };
    });
    
    this.markerClusterer.addMarker(marker);
  },

  clear_all_markers: function(){
    this.markerClusterer.clearMarkers();
  },
  test_markers: function() {
    var row, cell;
    var _lat = 32.7;
    var _lon = -117.1;
    var _offset = 0.5; // for randomly shifting points around the map
    var _text;
    for (var i = 0; i < 5; i++) {
      _text = "Marker #" + i.toString();
      // row = asset_table.insertRow(-1);
      // cell = row.insertCell(-1);
      // cell.innerHTML = _text
      this.create_marker(_lat, _lon, null, _text,"<P>Insert HTML here.</P>", null);

      _lat = _lat + _offset;
      _lon = _lon + _offset;
    }
  },
});


IONUX.Views.DashboardTable = IONUX.Views.DataTable.extend({
  initialize: function() {
    _.bindAll(this);
    this.$el.show();
    this.blacklist = this.options.list_table ? IONUX.ListWhitelist : IONUX.MapBlacklist;
    this.filter_data();
    this.collection.on('data:filter_render', this.filter_and_render);
    IONUX.Views.DataTable.prototype.initialize.call(this);
  },
  
  filter_data: function() {
    this.options.data = [];
    if (!_.isEmpty(this.blacklist)) {
       _.each(this.collection.models, function(resource) {
         if (!_.contains(this.blacklist, resource.get('type_')) && 
             !_.contains(this.blacklist, resource.get('lcstate'))) {
           this.options.data.push(resource.toJSON());
         };
       }, this);
    } else {
      this.options.data = this.collection.toJSON();
    };
  },
  
  filter_and_render: function() {
    this.filter_data();
    this.render();
  },
});


IONUX.Views.ResourceTable = IONUX.Views.DataTable.extend({
  initialize: function() {
    console.log('whitelist');
    _.bindAll(this);
    this.$el.show();
    this.whitelist = IONUX.ListWhitelist;
    this.filter_data();
    this.collection.on('data:filter_render', this.filter_and_render);
    IONUX.Views.DataTable.prototype.initialize.call(this);
  },
  
  filter_data: function() {
    this.options.data = [];
    if (!_.isEmpty(this.whitelist)) {
       _.each(this.collection.models, function(resource) {
         if (_.contains(this.whitelist, resource.get('type_'))) {
           this.options.data.push(resource.toJSON());
         };
       }, this);
    } else {
      this.options.data = []; //this.collection.toJSON();
    };
  },
  
  filter_and_render: function() {
    this.filter_data();
    this.render();
  },
});



/* 
- - - - - - - - - - - - - - - - - 
  Map Filters
- - - - - - - - - - - - - - - - - 
*/

IONUX.MapBlacklist = [];

IONUX.Views.MapFilter = Backbone.View.extend({
  el: '#map-filter',
  filter_options: {
    short_asset_options: [
      {label: 'Station', type: 'PlatformSite'},
      {label: 'Instrument', type: 'InstrumentSite'},
      {label: 'Platform', type: 'PlatformDevice'},
    ],
    long_asset_options: [
      {label: 'Station', type: 'PlatformSite'},
      {label: 'Instrument', type: 'InstrumentSite'},
      {label: 'Platform', type: 'PlatformDevice'},
    ],
    data_options: [
      {label: 'Data Products', type: 'DataProduct'}
    ],
    lcstate_options: [
      {label: 'Draft', lcstate: 'DRAFT'},
      {label: 'Planned', lcstate: 'PLANNED'},
      {label: 'Integrated', lcstate: 'INTEGRATED'},
      {label: 'Deployed', lcstate: 'DEPLOYED'},
      {label: 'Retired', lcstate: 'RETIRED'}
    ]
  },
  template: '\
    <h3>Selector\
      <!-- <span class="dropdown pull-right">\
        <a data-toggle="dropdown" href="#">DD</a>\
        <ul class="dropdown-menu">\
          <li><a class="show-short-list btn-navigation-plain" href="#">Short List</a></li>\
          <li><a class="show-long-list btn-navigation-plain" href="#">Long List</a></li>\
        </ul>\
      </span> -->\
    </h3>\
    <div class="panelize">\
      <input id="radio-assets" type="radio" name="map_filter" value="asset" checked />&nbsp;Asset&nbsp;\
      <input id="radio-data" type="radio" name="map_filter" value="data" />&nbsp;Data&nbsp;\
    </div>\
    <div id="asset-filter" class="panelize"></div>\
    <h3>Lifecycle</h3>\
    <div id="lcstate-filter" class="panelize"></div>\
  ',

  events: {
    'click .filter-option': 'set_filter'
  },
  
  initialize: function(){
    _.bindAll(this);
  },
  
  render: function(){
    this.$el.show().html(this.template);
    this.render_filter_options();
    return this;
  },
  
  render_filter_options: function(options){
    // Should not be in separate templates? 
    // Waiting for definitive filter behavior before consolidating.
    var item_tmpl = '<div class="filter-option"><%= label %> <input type="checkbox" value="<%= type %>" <%= checked %> /></div>';
    var lcstate_tmpl = '<div class="filter-option"><%= label %> <input type="checkbox" value="<%= lcstate %>" <%= checked %> /></div>';

    var assets_elmt = this.$el.find('#asset-filter');
    _.each(this.filter_options.short_asset_options, function(option) {
      option['checked'] = _.contains(IONUX.MapBlacklist, option['type']) ? "" : "checked";
      assets_elmt.append(_.template(item_tmpl, option));
    });
    
    var lcstate_elmt = this.$el.find('#lcstate-filter');
    _.each(this.filter_options.lcstate_options, function(option) {
      option['checked'] = _.contains(IONUX.MapBlacklist, option['lcstate']) ? "" : "checked";
      lcstate_elmt.append(_.template(lcstate_tmpl, option));
    });
    
    // Waiting for resource_registry calls
    // var data_elmt = this.$el.find('#data-filter');
    // _.each(this.filter_options.data_options, function(option) {
    //   data_elmt.append(_.template(item_tmpl, option));
    // });
  },
  
  toggle_filter: function(e) {
    this.$el.toggleClass('data-filter');
  },
  
  set_filter: function(e){
    console.log('set_filter');
    var filter_elmt = $(e.target);
    var type = filter_elmt.val();
    if (filter_elmt.is(':checked')) {
      var index = IONUX.MapBlacklist.indexOf(type)
      IONUX.MapBlacklist.splice(index);
    } else {
      IONUX.MapBlacklist.push(type);
    }; 
    IONUX.Dashboard.MapResources.trigger('data:filter_render');
  },
});


/* 
- - - - - - - - - - - - - - - - - 
  Asset List
- - - - - - - - - - - - - - - - - 
*/

IONUX.Collections.ListResources = Backbone.Collection.extend({
  initialize: function(models, options){
    this.resource_id = options.resource_id;
  },
  url: function() {
   return '/related_objects/'+this.resource_id+'/';
  },
  parse: function(resp) {
    var related_objects = [];
    _.each(resp.data, function(obj){related_objects.push(obj)});
    return related_objects;
  }
});

// IONUX.Views.AssetList = Backbone.View.extend({
//   el: '#2163993',
// 
//   initialize: function(){
//     _.bindAll(this);
//     this.collection.on('reset', this.render_table);
//   },
// 
//   render: function(){
//     this.$el.show();
//     return this;
//   },
//   
//   render_table: function(){
//     console.log('render_table');
//     
//     new IONUX.Views.DataTable({el: this.$el, data: this.collection.toJSON()});
//     
//     // if (!_.isEmpty(IONUX.MapBlacklist)) {
//     //   var filtered_resources = []
//     //   _.each(IONUX.Dashboard.ListResources.models, function(resource) {
//     //     if (!_.contains(IONUX.MapBlacklist, resource.get('type_')) && !_.contains(IONUX.MapBlacklist, resource.get('lcstate'))) {
//     //       filtered_resources.push(resource.toJSON());
//     //     };
//     //   });
//     //   new IONUX.Views.DataTable({el: this.$el, data: filtered_resources});
//     // } else {
//     //   new IONUX.Views.DataTable({el: this.$el, data: this.collection.toJSON()});
//     // };
//   },
// });

/* 
- - - - - - - - - - - - - - - - - 
  List Filter
- - - - - - - - - - - - - - - - - 
*/

IONUX.ListWhitelist = ['DataProduct', 'InstrumentDevice', 'PlatformDevice', 'PlatformSite', 'StationSite', 'Observatory'];

IONUX.Views.ListFilter = Backbone.View.extend({
  el: '#list-filter',
  filter_options: {
    short_list: [
      {label: 'Data Product', type: 'DataProduct'},
      {label: 'Instrument', type: 'InstrumentDevice'},
      {label: 'Platform', type: 'PlatformDevice'},
      {label: 'Station', type: 'PlatformSite'},
      {label: 'Site', type: 'Observatory'},
    ],
    long_list: [
      {label: 'Data Products', type: 'DataProduct'}
    ]
  },
  template: '\
    <h3>Resource Type</h3>\
    <div class="panelize">\
      <div id="long-filter"></div>\
      <div id="short-filter"></div>\
    </div>',
  item_template: _.template('<div class="filter-option">\
                             <%= label %> <input type="checkbox" value="<%= type %>" <%= checked %> />\
                             </div>'),
  events: {
    'click .filter-option input': 'set_filter'
  },
  
  initialize: function() {
    _.bindAll(this);
  },
  
  render: function() {
    this.$el.show().html(this.template);
    this.render_short_list();
    return this;
  },
  
  render_short_list: function() {
    var long_list = this.$el.find('#long-filter');
    _.each(this.filter_options.short_list, function(option) {
      option['checked'] = _.contains(IONUX.ListWhitelist, option['type']) ? "checked" : "";
      long_list.append(this.item_template(option));
    }, this);
  },
  
  set_filter: function(e){
    console.log('set_filter');
    var filter_elmt = $(e.target);
    var type = filter_elmt.val();
    if (filter_elmt.is(':checked')) {
      IONUX.ListWhitelist.push(type);
    } else {
      var index = IONUX.ListWhitelist.indexOf(type)
      IONUX.ListWhitelist.splice(index, 1);
    }; 
    IONUX.Dashboard.ListResources.trigger('data:filter_render');
    console.log(IONUX.ListWhitelist);
  },
});
