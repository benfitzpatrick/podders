<?php
App::uses('AppModel', 'Model');
/**
 * Resource Model
 *
 * @property Discipline $Discipline
 * @property Indudtry $Indudtry
 * @property Tag $Tag
 */
class Resource extends AppModel {

/**
 * Display field
 *
 * @var string
 */
	public $displayField = 'title';


	//The Associations below have been created with all possible keys, those that are not needed can be removed

/**
 * hasAndBelongsToMany associations
 *
 * @var array
 */
	public $hasAndBelongsToMany = array(
		'Discipline' => array(
			'className' => 'Discipline',
			'joinTable' => 'resources_disciplines',
			'foreignKey' => 'resource_id',
			'associationForeignKey' => 'discipline_id',
			'unique' => 'keepExisting',
			'conditions' => '',
			'fields' => '',
			'order' => '',
			'limit' => '',
			'offset' => '',
			'finderQuery' => '',
			'deleteQuery' => '',
			'insertQuery' => ''
		),
		'Indudtry' => array(
			'className' => 'Indudtry',
			'joinTable' => 'resources_indudtries',
			'foreignKey' => 'resource_id',
			'associationForeignKey' => 'indudtry_id',
			'unique' => 'keepExisting',
			'conditions' => '',
			'fields' => '',
			'order' => '',
			'limit' => '',
			'offset' => '',
			'finderQuery' => '',
			'deleteQuery' => '',
			'insertQuery' => ''
		),
		'Tag' => array(
			'className' => 'Tag',
			'joinTable' => 'resources_tags',
			'foreignKey' => 'resource_id',
			'associationForeignKey' => 'tag_id',
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
