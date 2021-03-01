import React from 'react';
import { ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import PeopleIcon from '@material-ui/icons/People';
import DashboardIcon from '@material-ui/icons/Dashboard';
import AssignmentIcon from '@material-ui/icons/Assignment';
import QuestionAnswerIcon from '@material-ui/icons/QuestionAnswer';
import { Link } from "react-router-dom";

export const ListItems = (
  <div className="list-item-container">
  <ListItem button component={Link} to="/dashboard">
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </ListItem>
    <ListItem button component={Link} to="/dashboard/rooms">
      <ListItemIcon>
        <QuestionAnswerIcon />
      </ListItemIcon>
      <ListItemText primary="Question" />
    </ListItem>
    <ListItem button component={Link} to="/dashboard/users">
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Users" />
    </ListItem>
    <ListItem button component={Link} to="/dashboard/events">
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Exam" />
    </ListItem>
  </div>
);