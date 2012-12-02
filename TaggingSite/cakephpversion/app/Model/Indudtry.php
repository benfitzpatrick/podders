<?php
App::uses('AppModel', 'Model');
/**
 * Indudtry Model
 *
 * @property Resource $Resource
 */
class Indudtry extends AppModel {

/**
 * Display field
 *
 * @var string
 */
	public $displayField = 'name';


	//The Associations below have been created with all possible keys, those that are not needed can be removed

/**
 * hasAndBelongsToMany associations
 *
 * @var array
 */
	public $hasAndBelongsToMany = array(
		'Resource' => array(
			'className' => 'Resource',
			'joinTable' => 'resources_indudtries',
			'foreignKey' => 'indudtry_id',
			'associationForeignKey' => 'resource_id',
			'unique' => 'keepExisting',
			'conditions' => '',
			'fields' => '',
			'order' => '',
			'limit' => '',
			'offset' => '',
			'finderQuery' => '',
			'deleteQuery' => '',
			'insertQuery' => ''
		)
	);

}
