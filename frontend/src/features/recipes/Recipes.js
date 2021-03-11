import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';

export function Recipes() {
    const dispatch = useDispatch();
    return (
        <div>
            <h1>
                Recipes
            </h1>
        </div>
    );
}
