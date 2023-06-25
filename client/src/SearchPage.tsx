import * as React from 'react';
import Box from '@mui/material/Box';
import Header from './Header';
import Filter from './Filter';
import SearchBlock from './SearchBlock';
import Card from './Card';
import {CardsBlock, CardsBlockItem} from './CardsBlock';
import { styled } from '@mui/system';
import axios from 'axios';
import useId from '@mui/material/utils/useId';

type Room = {
    description : string,
    id: number,
    price: number,
    rate: number,
    subtitle: string,
    title: string,
    image: string
};

type TypesOfHousing = {
    house: boolean,
    flat: boolean,
    villa: boolean,
    hotel: boolean
};

const server = 'http://rusbnb-1.exp-of-betrayal.repl.co';

const Content = styled(Box)({
    display: 'flex', flexDirection: 'row', width: '79.8vw', marginLeft: '12vw', marginTop: '5vh', justifyContent: 'space-between'
})

export default function SearchPage (){
    const filterCost : number = Number(localStorage.getItem('filterCost') || '35000'),
    filterCount : number= Number(localStorage.getItem('filterCount') || '1'),
    filterTypes : TypesOfHousing = JSON.parse(localStorage.getItem('filterTypes') || JSON.stringify({
        house: true,
    flat: true,
    villa: true,
    hotel: true
    }));
    const [rooms, setRooms] = React.useState(Array<Room>);
    axios.get(server+'/rooms'
    )
    .then(res=>{
            setRooms(res.data.rooms);
        })
        .catch((error) => {
            console.log(error)
            if (error.response){
                console.log(error.response.data);
                
                }else if(error.request){
                    console.log(1);
                    console.log(error.request)
                
                }else if(error.message){
                    console.log(2);
                    console.log(error.message)
                
                }
          });

    const id = useId();
    
    return (
        <>
        <SearchBlock />
            <Content>
                <Filter />
                <CardsBlock container sx={{width: '60vw', marginLeft: '0vw'}}>
                {
                    rooms.map((room, index)=>(
                        
                    ((filterTypes.house && room.title.toLowerCase().includes("дом")) ||
                    (filterTypes.flat && room.title.toLowerCase().includes("квартира"))||
                    (filterTypes.villa && room.title.toLowerCase().includes("вилла"))||
                    (filterTypes.hotel && room.title.toLowerCase().includes("отель"))) &&
                    (room.price <= filterCost)?
                    (<>
                    <CardsBlockItem item key={`${id}-${index}`}>
                        <Card 
                        imgSrc='https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/99/ec/e0/getlstd-property-photo.jpg?w=1200&h=-1&s=1'
                        cost={room.price} rating={room.rate}
                        type={room.title} place={room.subtitle}
                        desc={room.description}
                        id={room.id}
                        />
                    </CardsBlockItem>
                    </>):(<></>)))
                    }
            </CardsBlock>
            </Content>
        </>
    )
}
